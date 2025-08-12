import pygame
import Managers.univars as univars
import moderngl
from array import array
import random

#CREDIT TO DAFLUFFYPOTATO FOR SHADER CODE

ctx = moderngl.create_context()
bgctx = moderngl.create_context()
quad_buffer = ctx.buffer(data = array('f',[
    -1.0,1.0,0.0,0.0,
    1.0,1.0,1.0,0.0,
    -1.0,-1.0,0.0,1.0,
    1.0,-1.0,1.0,1.0,
]))
bgquad_buffer = bgctx.buffer(data = array('f',[
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
tex = ctx.texture(univars.realscreeen.get_size(), int(4))
tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
tex.swizzle = 'BGRA'



def surf_to_texture(surf):
    tex.write(surf.get_view('1'))
    return tex



with open("Bgshader.fs","r") as code:
    bg_frag_shader = code.read()


bgprogram = bgctx.program(vertex_shader=vert_shader,fragment_shader=bg_frag_shader)
bgrender_object = bgctx.vertex_array(bgprogram, [(bgquad_buffer, '2f 2f', 'vert', 'texcoord')])


def bg_surf_to_texture(surf):
    bgtex = bgctx.texture(surf.get_size(), int(4))
    bgtex.filter = (moderngl.NEAREST, moderngl.NEAREST)
    bgtex.swizzle = 'BGRA'
    bgtex.write(surf.get_view('1'))
    return bgtex
