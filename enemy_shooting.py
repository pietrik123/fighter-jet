import bge
import mathutils

cont = bge.logic.getCurrentController()

owner = cont.owner

target = bge.logic.getSceneList()[0].objects['FighterJet']

vect  = mathutils.Vector((\
target.worldPosition[0] - owner.worldPosition[0], \
target.worldPosition[1] - owner.worldPosition[1], \
target.worldPosition[2] - owner.worldPosition[2] \
))

angle = owner.getAxisVect(mathutils.Vector((0.0,0.0,1.0))).angle(vect)
if angle < 0.1:
    cont.activate(owner.actuators[0])
else:
    cont.deactivate(owner.actuators[0])