from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from core.classes.Hand import Hand

from core.classes.Blocks import blocks


app=Ursina()
#window.fullscreen=True
window.fps_counter.enabled=False
window.exit_button.enabled=True

for z in range(20):
    for x in range(20):
            blocks(position=(x,0,z))

initPlayer=FirstPersonController()

ski = Sky()
hand = Hand()

app.run()