# script for control of enemy missile (version 2)
import bge
from mathutils import *

scene = bge.logic.getCurrentScene()

missile = bge.logic.getCurrentController().owner

fighter = scene.objects['FighterJet']
print("Enemy missile script! (2)")

if 'init' not in missile: 
	missile.visible = False
	missile.children[0].visible = False
	missile['init'] = 1
	
if missile['launched'] == False:
	if scene.objects['Main']['timer0'] > missile['startTime']:	
		missile.setLinearVelocity(Vector((0.0,0.0,100.0)),True)
		
		if 'target' not in missile:
			missile['target'] = None
		missile.visible = True
		missile.children[0].visible = True
		missile['launched'] = True
        
		translateVect = fighter.worldOrientation*Vector((-1500.0,0,0))		
		missile.worldPosition = [fighter.worldPosition[0]+translateVect[0],fighter.worldPosition[1]+translateVect[1],fighter.worldPosition[2]+translateVect[2]+100.0]
		
		print(fighter.worldPosition)
		print(missile.worldPosition)
		
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

print('*****************')
		
		
		