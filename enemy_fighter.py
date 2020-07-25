# control script for an enemy jet, which follows the player
import bge
import mathutils

owner = bge.logic.getCurrentController().owner

scene = bge.logic.getSceneList()[0]

fighter = scene.objects['FighterJet']

direction = mathutils.Vector(( \
	fighter.worldPosition[0] - owner.worldPosition[0],\
	fighter.worldPosition[1] - owner.worldPosition[1],\
	fighter.worldPosition[2] - owner.worldPosition[2]
))

direction.normalize()

angleToOwnerXAxis = direction.angle(owner.getAxisVect(mathutils.Vector((1.0,0.0,0.0))))

distance = owner.getDistanceTo(fighter)

setDistance = 50

error = distance - setDistance

# factor - amplification
k = 2 

speedSet = k*error

speedMax = 250
speedMin = 100

if speedSet > speedMax:
	speedSet = speedMax

if speedSet < speedMin:
	speedSet = speedMin
	
owner.setLinearVelocity(mathutils.Vector((speedSet,0,0)),True)

deltaRotation = 0.05

if angleToOwnerXAxis > 0.01:
	factor = deltaRotation/angleToOwnerXAxis
else:
	factor = 1.0

owner.alignAxisToVect(direction,0,factor)

