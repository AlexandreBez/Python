from ursina import *

hand_texture = load_texture('interface\objects_texture\arm_texture.png')

class Hand(Entity):

    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='arm',
            texture=hand_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.5, -0.6)
        )

    def active(self):
        self.position=Vec2(0.4, -0.5)

    def passive(self):
        self.position=Vec2(0.5, -0.6)