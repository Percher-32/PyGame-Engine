#version 330 core
uniform sampler2D tex;
uniform float time;
uniform float pacify;
uniform int state;
uniform vec2 sunpos;
uniform float illuminace;
uniform float waterlevel;
uniform float camx;




in vec2 uvs;
out vec4 f_color;


vec2 randomGradient(vec2 p) {
  p = p + 0.02;
  float x = dot(p, vec2(123.4, 234.5));
  float y = dot(p, vec2(234.5, 345.6));
  vec2 gradient = vec2(x, y);
  gradient = sin(gradient);
  gradient = gradient * 43758.5453;

  // part 4.5 - update noise function with time
  gradient = sin(gradient + time/10);
  return gradient;

  // gradient = sin(gradient);
  // return gradient;
}

// inigo quilez - https://iquilezles.org/articles/distfunctions2d/
float sdfCircle(in vec2 p, in float r) {
  return length(p) - r;
}

// inigo quilez - https://iquilezles.org/articles/distfunctions2d/
float sdfOrientedBox(in vec2 p, in vec2 a, in vec2 b, float th) {
  float l = length(b - a);
  vec2 d = (b - a) / l;
  vec2 q = (p - (a + b) * 0.5);
  q = mat2(d.x, -d.y, d.y, d.x) * q;
  q = abs(q) - vec2(l, th) * 0.5;
  return length(max(q, 0.0)) + min(max(q.x, q.y), 0.0);
}

vec2 cubic(vec2 p) {
  return p * p * (3.0 - p * 2.0);
}

vec2 quintic(vec2 p) {
  return p * p * p * (10.0 + p * (-15.0 + p * 6.0));
}

float perlin() {
  // part 0 - basic shader setup
  vec2 uv = uvs;
  uv.x += camx;


  vec3 black = vec3(0.0);
  vec3 white = vec3(1.0);
  vec3 color = black;

  // part 1 - set up a grid of cells
  uv = uv * 4.0;
  vec2 gridId = floor(uv);
  vec2 gridUv = fract(uv);
  color = vec3(gridId, 0.0);
  color = vec3(gridUv, 0.0);

  // part 2.1 - start by finding the coords of grid corners
  vec2 bl = gridId + vec2(0.0, 0.0);
  vec2 br = gridId + vec2(1.0, 0.0);
  vec2 tl = gridId + vec2(0.0, 1.0);
  vec2 tr = gridId + vec2(1.0, 1.0);

  // part 2.2 - find random gradient for each grid corner
  vec2 gradBl = randomGradient(bl);
  vec2 gradBr = randomGradient(br);
  vec2 gradTl = randomGradient(tl);
  vec2 gradTr = randomGradient(tr);

  // part 2.3 - visualize gradients (for demo purposes)
  vec2 gridCell = gridId + gridUv;
  float distG1 = sdfOrientedBox(gridCell, bl, bl + gradBl / 2.0, 0.02);
  float distG2 = sdfOrientedBox(gridCell, br, br + gradBr / 2.0, 0.02);
  float distG3 = sdfOrientedBox(gridCell, tl, tl + gradTl / 2.0, 0.02);
  float distG4 = sdfOrientedBox(gridCell, tr, tr + gradTr / 2.0, 0.02);
  if (distG1 < 0.0 || distG2 < 0.0 || distG3 < 0.0 || distG4 < 0.0) {
    color = vec3(1.0);
  }

  // part 3.1 - visualize a single center pixel on each grid cell
  float circleRadius = 0.025;
  vec2 circleCenter = vec2(0.5, 0.5);
  float distToCircle = sdfCircle(gridUv - circleCenter, circleRadius);
  color = distToCircle > 0.0 ? color : white;

  // part 3.2 - find distance from current pixel to each grid corner
  vec2 distFromPixelToBl = gridUv - vec2(0.0, 0.0);
  vec2 distFromPixelToBr = gridUv - vec2(1.0, 0.0);
  vec2 distFromPixelToTl = gridUv - vec2(0.0, 1.0);
  vec2 distFromPixelToTr = gridUv - vec2(1.0, 1.0);

  // part 4.1 - calculate the dot products of gradients + distances
  float dotBl = dot(gradBl, distFromPixelToBl);
  float dotBr = dot(gradBr, distFromPixelToBr);
  float dotTl = dot(gradTl, distFromPixelToTl);
  float dotTr = dot(gradTr, distFromPixelToTr);

  // part 4.4 - smooth out gridUvs
  // gridUv = smoothstep(0.0, 1.0, gridUv);
  // gridUv = cubic(gridUv);
  gridUv = quintic(gridUv);

  // part 4.2 - perform linear interpolation between 4 dot products
  float b = mix(dotBl, dotBr, gridUv.x);
  float t = mix(dotTl, dotTr, gridUv.x);
  float perlin = mix(b, t, gridUv.y);

  // part 4.3 - display perlin noise
  // color = distToCircle > 0.0 ? color : white;
  // if (distG1 < 0.0 || distG2 < 0.0 || distG3 < 0.0 || distG4 < 0.0) {
  //   color = vec3(1.0);
  // }

  // part 4.5 - update randomGradient function with time

  // part 5.1 - billow noise
  // float billow = abs(perlin);
  // color = vec3(billow);

  // part 5.2 - ridged noise
  // float ridgedNoise = 1.0 - abs(perlin);
  // ridgedNoise = ridgedNoise * ridgedNoise;
  // color = vec3(ridgedNoise);

  return perlin;
}

float coldist(vec2 uv){
  vec3 map = texture(tex, uv).rgb;
  return distance(vec3(0,0,0),map);
}


void main() {
    float pixelscale = 0.0001;
    vec2 sample_pos = uvs;
    sample_pos = round(sample_pos /vec2(pixelscale)) * vec2(pixelscale);
    sample_pos.x = clamp(sample_pos.x ,0,1);
    vec3 map = texture(tex, sample_pos).rgb;
    
    

    if (state == 0){
        
        vec2 fakeuvs = vec2(uvs.x-0.5 ,uvs.y-0.5 );

        vec2 slighttwist = vec2(sin(time/40) + 0.5,cos(time/40) + 0.5);
        float twistval = 0.4;

        //1 on outside  , 0 on inside
        float dist = abs(distance(vec2(0,0),fakeuvs));
        // dist = 0;
        // 0 near sun   1 away from sun
        vec2 sunposoff = vec2(sunpos.x + 0.5,sunpos.y + 0.5);
        float sundist = abs(distance(uvs,sunposoff));


        float twistsiist = abs(distance(uvs,slighttwist));
        //0 on outside  , 1 on inside
        float dark = 1 - ((sundist/(illuminace * 2)) + dist/2)/2 - pacify;
        float hurt = 0;
        vec2 sampling = vec2(sample_pos.x + 0.01,sample_pos.y);
        float vigb = mix((1 - dist/3),dark,hurt);
        float vigr = mix(dark,(1 - dist/5),hurt);
        float offsetsine =  sin(sin((uvs.x + camx) + time/1000)*20 + time/100  + 2*sin( time/1000)/25     + sin( sin(time/300) + (uvs.x + camx))/20                )/50;
        offsetsine = perlin()/20;



        if (uvs.y > (1-waterlevel) + offsetsine || map == vec3(255,0,0)) {
            float fwl = waterlevel;
            if (fwl > 0.5){
              fwl = 0.5;
            }
            vec2 reflec_sample_pos = vec2(uvs.x  + sin(time/10 + (uvs.y) * 50)/800+ perlin()/50,(1-fwl) - abs((1-fwl)- uvs.y)- perlin()/50 );
            vec2 underwater_sample_pos = vec2(uvs.x  + sin(time/10 + (uvs.y) * 50)/800,uvs.y+ cos(time/20 + (uvs.x) * 50)/800);



            float reflec_dark = dark * (0.5 + perlin()/5);
            float underwater_dark = dark * (0.7 + perlin()/4) + (1-uvs.y)/10 ;
            if (distance(map,vec3(0,0,0)) > 20){
              underwater_dark = 1;
            }



            underwater_sample_pos.x = clamp(underwater_sample_pos.x + perlin()/60,0,0.99);
            underwater_sample_pos.y = clamp(underwater_sample_pos.y + perlin()/60,0,0.99);


            reflec_sample_pos.x = clamp(reflec_sample_pos.x ,0,1);
            // reflec_sample_pos.y = clamp(reflec_sample_pos.y ,0,1);

            underwater_sample_pos = round(underwater_sample_pos /vec2(pixelscale)) * vec2(pixelscale);
            reflec_sample_pos = round(reflec_sample_pos /vec2(pixelscale)) * vec2(pixelscale);


            float scalar = 2*(1- waterlevel) +0.2;

            if (scalar < 0){
              scalar = 0;
            }
            if (scalar > 1){
              scalar = 1;
            }
            
            scalar = pow(scalar,3);

            // scalar = mix(0,scalar,scalar);

            dark = mix(reflec_dark,underwater_dark,1-scalar);
            map = mix(  texture(tex, underwater_sample_pos).rgb   ,  texture(tex, reflec_sample_pos).rgb  ,  scalar  );
            vigb = mix((1 - dist/5),dark,hurt);
            vigr = mix(dark,dark*2,hurt);

            
        }

        // if ( texture(tex,uvs).rgb * vec3(255,255,255) == vec3(0,0.,255)){
        //   float fwl = 0.5;
        //   vec2 sample_pos = vec2(uvs.x  + sin(time/10 + (uvs.y) * 50)/8+ perlin(),(1-fwl) - abs((1-fwl)- uvs.y)- perlin() );
        //   dark *= (0.5 + perlin()/5)/10;
        //   vigb = mix((1 - dist/5),dark,hurt);
        //   vigr = mix(dark,dark*2,hurt);
        //   map = texture(tex, sample_pos).rgb;
        // }

        f_color = vec4(map.r  * vigr ,map.g * dark,map.b * vigb   , 0 + (time*0));

    }
    else{
        f_color = vec4(texture(tex, uvs).rgb, 1.0);
    }
}