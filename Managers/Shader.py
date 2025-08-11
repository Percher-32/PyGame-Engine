import pygame
import Managers.univars as univars
import moderngl
from array import array
import random

#CREDIT TO DAFLUFFYPOTATO FOR SHADER CODE

ctx = moderngl.create_context()
quad_buffer = ctx.buffer(data = array('f',[
    -1.0,1.0,0.0,0.0,
    1.0,1.0,1.0,0.0,
    -1.0,-1.0,0.0,1.0,
    1.0,-1.0,1.0,1.0,
]))


vert_shader = """
#version 330 core

in vec2 vert;
in vec2 texcoord;
out vec2 uvs;


void main() {
    uvs = texcoord;
    gl_Position = vec4(vert,0.0,1.0);
}

"""



frag_shader = """
#version 330 core

uniform sampler2D tex;

in vec2 uvs;
out vec4 f_color; 

void main(){
    f_color = vec4(texture(tex,uvs).rgb,1.0);
}
"""


program = ctx.program(vertex_shader=vert_shader,fragment_shader=frag_shader)
render_object = ctx.vertex_array(program, [(quad_buffer, '2f 2f', 'vert', 'texcoord')])


def surf_to_texture(surf):
    # size = univars.finalscreen.get_size()
    tex = ctx.texture(surf.get_size(), 4)
    tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
    tex.swizzle = 'BGRA'
    tex.write(surf.get_view('1'))
    return tex
