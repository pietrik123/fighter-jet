# script used for collision handling of enemy vehicles
import bge
from mathutils import Vector
import math

owner = bge.logic.getCurrentController().owner

if 'hitByMissile' not in owner:
	owner['hitByMissile'] = False
	owner['explosionAfterHitAdded'] = False
	owner['hitGround'] = False
	owner['explosionAfterGroundHitAdded'] = False

else:
	scene = bge.logic.getCurrentScene()
	
	for obj in scene.objects:
		if 'missile' in obj.name:
			if obj.getDistanceTo(owner) < 20.0:
				owner['hitByMissile'] = True
					
	if owner['hitByMissile'] == False:
		
		owner.setLinearVelocity(Vector((150.0,0.0,0.0)))
			
	if owner['hitByMissile'] == True and owner['explosionAfterHitAdded'] == False:
		owner['explosionAfterHitAdded'] = True
				
		explosion = scene.addObject('Explosion',owner,100)
		
		explosion['size'] = 5.0
		owner.applyRotation(Vector((math.radians(10.0),math.radians(15.0),math.radians(10.0))))
		owner.setAngularVelocity(Vector((0.5,0.0,0.0)))
			
	if owner['hitGround'] == True and owner['explosionAfterGroundHitAdded'] == False:		
		owner['explosionAfterGroundHitAdded'] = True
				
		explosion = scene.addObject('Explosion',owner,100)
		
		explosion['size'] = 8.0
		owner.worldPosition = [0.0,0.0,-1000.0]
		owner.suspendDynamics()