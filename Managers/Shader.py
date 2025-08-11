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


with open("Shadercode.fs","r") as code:
    frag_shader = code.read()


program = ctx.program(vertex_shader=vert_shader,fragment_shader=frag_shader)
render_object = ctx.vertex_array(program, [(quad_buffer, '2f 2f', 'vert', 'texcoord')])


def surf_to_texture(surf):
    tex = ctx.texture(surf.get_size(), 4)
    tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
    tex.swizzle = 'BGRA'
    tex.write(surf.get_view('1'))
    return tex
