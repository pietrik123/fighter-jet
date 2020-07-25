import bge
from mathutils import *

fighter = bge.logic.getCurrentController().owner
scene = bge.logic.getCurrentScene()
shadow = scene.objects['FighterShadow']

raySensor = fighter.sensors['RaySensor']

hitPos = raySensor.hitPosition
hitPos[2] = hitPos[2] + 0.5

start = fighter.worldPosition
end = (start[0],start[1],-1000.0)

obj, hitPoint, hitNormal = fighter.rayCast(end,start,400.0,"reflectRays",1,0)

fighterXAxis = fighter.getAxisVect(Vector((1.0,0.0,0.0)))

fighterXAxisXY =  Vector((fighterXAxis[0],fighterXAxis[1],0.0))

if hitPoint != None:
    hitPoint[2] = hitPoint[2] + 0.5
    shadow.worldPosition = hitPoint
shadow.alignAxisToVect(fighterXAxisXY,0,1.0)

print("*******Fighter shadow script**************")
print(hitPos)
print("******************************************")