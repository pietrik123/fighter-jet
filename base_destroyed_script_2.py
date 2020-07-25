# script used for smoke emitter of object 'EnemyBaseCenter'
# smoke is emitted 
import bge
import random

cont = bge.logic.getCurrentController()
owner = cont.owner
scene = bge.logic.getCurrentScene()

base =  scene.objects['EnemyBaseCenter']

if 'init' not in owner:
	owner['init'] = True	
	random.seed(None)

speed = random.randint(20,40)
time = random.randint(80,130)
	
owner.actuators[0].time = time
owner.actuators[0].linearVelocity = [0,0,speed]

if base['energy'] > 1:
    # activate smoke emitter via controller
	cont.activate(owner.actuators[0])
else:
	cont.deactivate(owner.actuators[0])