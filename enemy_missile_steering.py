# script for control of enemy missile
import bge
from mathutils import *

scene = bge.logic.getCurrentScene()

missile = bge.logic.getCurrentController().owner

fighter = scene.objects['FighterJet']
print("Enemy missile script!")

if 'init' not in missile:
	missile.setLinearVelocity(Vector((100.0,0.0,0.0)),True)
	missile['init'] = 1
	
	if 'target' not in missile:
		missile['target'] = None		
else:	
	for obj in scene.objects:
		if 'flare' in obj:
			print("Flare detected!")
			if obj.getDistanceTo(missile) < 300.0:
				missile['target'] = obj
	
    print(missile['target'])			
	
	if 'destroyed' not in missile:
		if missile['target'] != None:
			missile.setLinearVelocity(Vector((400.0,0.0,0.0)),True)
			directionVect = Vector ( ( \
				missile['target'].worldPosition[0] - missile.worldPosition[0],
				missile['target'].worldPosition[1] - missile.worldPosition[1],
				missile['target'].worldPosition[2] - missile.worldPosition[2],
			))
			
			missile.alignAxisToVect(directionVect,0,0.15)

			if missile.getDistanceTo(missile['target']) < 15.0:				
				missile['destroyed'] = True
				missile.worldPosition = [0,0,-100]
						
				missile['target']['destroyed'] = True
