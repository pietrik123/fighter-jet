import math
from mathutils import *
import bge

print("Compass")

mainScene = bge.logic.getSceneList()[0]

owner = bge.logic.getCurrentController().owner

fighter = mainScene.objects['FighterJet']

fighterXAxis = fighter.getAxisVect(Vector((1.0,0.0,0.0)))

x = fighterXAxis[0]
y = fighterXAxis[1]

angle = math.atan2(y,x)

print(angle)

newOrientation = Matrix.Rotation(angle,3,'Z')
owner.worldOrientation = newOrientation