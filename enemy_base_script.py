import bge

owner = bge.logic.getCurrentController().owner
scene = bge.logic.getCurrentScene()

if 'init' not in owner:
	owner['init'] = True
	owner['energy'] = 100

#check collision with a missile

for obj in scene.objects:
	if 'missile' in obj.name:
		if obj.getDistanceTo(owner) < 20:
			if owner['energy'] > 0:
				owner['energy'] -= 25
			 
			 
	 
	 