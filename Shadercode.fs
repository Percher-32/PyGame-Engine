#version 330 core

uniform sampler2D tex;
uniform float time;

in vec2 uvs;
out vec4 f_color;

void main() {
    // vec2 sample_pos = uvs;
    vec2 sample_pos = vec2(uvs.x + sin((uvs.y * 10) + (time*2) * 0.1) * 0.02, uvs.y);
    vec3 map = texture(tex, sample_pos).rgb;
    f_color = vec4(map.r ,map.g,map.b, 1.0);
}