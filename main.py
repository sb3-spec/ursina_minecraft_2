from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from mesh_terrain import MeshTerrain

app = Ursina()

window.color = color.rgb(0, 200, 255)
indra = Sky()
indra.color = window.color
subject = FirstPersonController()

subject.gravity = 0

terrain = MeshTerrain()

terrain.genTerrain()

def update():
    block_found = False
    
    # Step up or down
    step = 2
    height = 1.86
    
    x = str(floor(subject.x + .5))
    z = str(floor(subject.z + .5))
    y = floor(subject.y + .5)
    
    for i in range(-step, step):
        location = f'x{x}y{str(y + i)}z{z}'
        if terrain.terrain_dict.get(location):
            target = y + i + height
            block_found = True
            break

            
    if block_found:
        subject.y = lerp(subject.y, target, 6 * time.dt)
    else:
        subject.y -= 9.8 * time.dt
        
    # BUTTON PRESSES

        
        
def input(key):
    if key == 'escape':
        quit()
        

app.run()