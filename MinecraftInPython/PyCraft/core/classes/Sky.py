from ursina import *
from ursina import entity
from ursina import texture

sky_texture=load_texture('\interface\objects_texture\skybox.png')

class Sky(entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model='sphere',
            texture=load_texture(sky_texture),
            scale=150,
            double_sided=True
        )