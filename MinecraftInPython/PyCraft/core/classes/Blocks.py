from ursina import audio, scene, texture
from ursina import *

from core.classes.Hand import Hand

grass_texture = 'interface\objects_texture\grass_block.png'
stone_texture = 'interface\objects_texture\stone_block.png'
brick_texture = 'interface\objects_texture\brick_block.png'
dirty_texture = '\interface\objects_texture\dirt_block.png'
block_pick=1
block_pick=2
block_pick=3
block_pick=4
punch_sound=audio('sounds\objects_sound\punch_sound.wav',loop=False, autoplay=False)

class blocks(Button):
    
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position= position,
            model= 'block',
            origin_y=0.5,
            texture= load_texture(grass_texture),
            color=color.white,
            highlight_color=color.lime,
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            # add blocks
            if key == 'left mouse down':
                punch_sound.play()
                if block_pick == 1: blocks(position=self.position + mouse.normal, texture=load_texture(grass_texture))
                if block_pick == 2: blocks(position=self.position + mouse.normal, texture=load_texture(stone_texture))
                if block_pick == 3: blocks(position=self.position + mouse.normal, texture=load_texture(brick_texture))
                if block_pick == 4: blocks(position=self.position + mouse.normal, texture=load_texture(dirty_texture))

            # broke blocks
            if key == 'right mouse down':
                punch_sound.play()
                destroy(self);
            # exit
            if key == 'q':
                exit()

def update():
    global block_pick

    if held_keys['left mouse'] or held_keys['right mouse']:
        Hand.active()
    else:
        Hand.passive()

    if held_keys['c']: block_pick=1
    if held_keys['v']: block_pick=2
    if held_keys['b']: block_pick=3
    if held_keys['n']: block_pick=4

