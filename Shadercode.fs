#version 330 core

uniform sampler2D tex;
uniform float time;
uniform int state;

in vec2 uvs;
out vec4 f_color;



void main() {
    // vec2 sample_pos = uvs;
    if (state == 0){
        
        vec2 fakeuvs = vec2(uvs.x-0.5,uvs.y-0.5);

        //1 on outside  , 0 on inside
        float dist = abs(distance(vec2(0,0),fakeuvs));
        //0 on outside  , 1 on inside
        float dark = 1 - dist/1.5;

        vec2 sample_pos = vec2(uvs.x ,uvs.y );
        vec3 map = texture(tex, sample_pos).rgb;
        f_color = vec4(map.r  * dark ,map.g * dark,map.b * (1 - dist/5)   , 0 + (time*0));
    }
    else{
        f_color = vec4(texture(tex, uvs).rgb, 1.0);
    }
}