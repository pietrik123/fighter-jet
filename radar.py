import math
from mathutils import *
import bge

print("Radar Sc")

mainScene = bge.logic.getSceneList()[0]
radarScene = bge.logic.getCurrentScene()

owner = bge.logic.getCurrentController().owner

fighter = mainScene.objects['FighterJet']

fighterInd = radarScene.objects['FighterInd']

if 'indicators' not in owner:
	owner['indicators'] = []
	obj = radarScene.addObject('EnemyIndRadar','Start')
	owner['indicators'].append(obj)
	obj = radarScene.addObject('EnemyIndRadar','Start')
	owner['indicators'].append(obj)
	obj = radarScene.addObject('EnemyIndRadar','Start')
	owner['indicators'].append(obj)
	obj = radarScene.addObject('EnemyIndRadar','Start')
	owner['indicators'].append(obj)
	obj = radarScene.addObject('EnemyIndRadar','Start')
	owner['indicators'].append(obj)
	obj = radarScene.addObject('MissileInd','Start')
	owner['indicators'].append(obj)
	obj = radarScene.addObject('MissileInd','Start')
	owner['indicators'].append(obj)
	obj = radarScene.addObject('MissileInd','Start')
	owner['indicators'].append(obj)

	owner['objects'] = []
	owner['objects'].append(mainScene.objects['Jet'])
	owner['objects'].append(mainScene.objects['Jet.001'])
	owner['objects'].append(mainScene.objects['Jet.002'])
	owner['objects'].append(mainScene.objects['Jet.003'])
	owner['objects'].append(mainScene.objects['Jet.004'])
	owner['objects'].append(mainScene.objects['EnemyMissile'])
	owner['objects'].append(mainScene.objects['EnemyMissile.001'])
	owner['objects'].append(mainScene.objects['EnemyMissile.002'])
	
else:	
	pass

fighterXAxis = fighter.getAxisVect(Vector((1.0,0.0,0.0)))

r = 1.0
R = 3000.0

indicators = owner['indicators']
objects = owner['objects']

for i in range(0,len(objects)):
	obj = objects[i]
	vect = [obj.worldPosition.x - fighter.worldPosition.x, obj.worldPosition.y - fighter.worldPosition.y]
	vect2 = [0,0]
	if (vect[0]**2.0 + vect[1]**2.0)**0.5 < R:
		vect2[0] = vect[0] *r/R
		vect2[1] = vect[1] *r/R
	else:	
		vect2[0] = vect[0]/((vect[0]**2.0 + vect[1]**2.0)**0.5) * r
		vect2[1] = vect[1]/((vect[0]**2.0 + vect[1]**2.0)**0.5) * r
		print(vect2[0])
		print(vect2[1])
		print((vect2[0]**2.0 + vect2[1]**2.0)**0.5)
	indicators[i].worldPosition = [fighterInd.worldPosition.x + vect2[0],fighterInd.worldPosition.y + vect2[1],indicators[i].worldPosition.z]
	indicators[i].visible = obj.visible
	if 'destroyed' in obj:
		indicators[i].visible = False
	if 'hitByMissile' in obj:
		if obj['hitByMissile'] == True:
			indicators[i].visible = False
