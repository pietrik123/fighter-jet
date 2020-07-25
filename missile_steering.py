# script used for steering of player's jet missile 
import bge
from mathutils import *

scene = bge.logic.getCurrentScene()

missile = bge.logic.getCurrentController().owner

print("Missile script!")

if 'init' not in missile:
    missile.setLinearVelocity(Vector((400.0,0.0,0.0)),True)
    missile['init'] = 1
    if 'target' not in missile:
        missile['target'] = None
else:
    if 'destroyed' not in missile:
        if missile['target'] != None:
            missile.setLinearVelocity(Vector((400.0,0.0,0.0)),True)
            directionVect = Vector ( ( \
                missile['target'].worldPosition[0] - missile.worldPosition[0],
                missile['target'].worldPosition[1] - missile.worldPosition[1],
                missile['target'].worldPosition[2] - missile.worldPosition[2],
            ))
            
            missile.alignAxisToVect(directionVect,0,0.1)
            
            print("*****Missile Script ok!!!")

            if missile.getDistanceTo(missile['target']) < 15.0:
                
                missile['destroyed'] = True
                missile.worldPosition = [0,0,-100]
        
        
        
        