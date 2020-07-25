# simple control script for enemy jet
import bge

owner = bge.logic.getCurrentController().owner

if 'initMovement' not in owner:
	 
	owner['initMovement'] = True
else:
	if owner['hitByMissile'] == False:
		if owner.getDistanceTo([0,0,0])) > 1500:
			owner.worldPosition = [owner['startX'],owner['startY'],owner['startZ']]	 
		else:
			owner.setLinearVelocity(Vector((150.0,0.0,0.0)),True)
			owner.setAngularVelocity(Vector((0.0,0.0,0.0)))