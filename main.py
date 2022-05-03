from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from mesh_terrain import MeshTerrain

app = Ursina()

window.color = color.rgb(200, 0, 255)
subject = FirstPersonController()

terrain = MeshTerrain()

terrain.genTerrain()

def update():
    pass

def input(key):
    if key == 'escape':
        quit()

app.run()