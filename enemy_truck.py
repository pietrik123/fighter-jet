import bge
import math

owner = bge.logic.getCurrentController().owner

if 'destroyed' not in owner:
	owner['destroyed'] = False
	owner['explosionAdded'] = False
	owner['hitByMissile'] = False

else:
	scene = bge.logic.getCurrentScene()
	
	for obj in scene.objects:
		if 'missile' in obj.name:
			if obj.getDistanceTo(owner) < 20.0:
				owner['destroyed'] = True
				owner['hitByMissile'] = True
	
	if owner['destroyed'] == True and owner['explosionAdded'] == False:
		explosion = scene.addObject('Explosion',owner,100)
		
		explosion['size'] = 6.0
		owner.worldPosition = [0.0,0.0,-1000.0]
		owner['explosionAdded'] = True