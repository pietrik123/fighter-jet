import bge
import mathutils

cont = bge.logic.getCurrentController()

resistanceVect = cont.owner

scene = bge.logic.getCurrentScene()

fighter = scene.objects['FighterJet']

resistanceVect.worldPosition = fighter.worldPosition

v = mathutils.Vector((-fighter['vx'],-fighter['vy'],-fighter['vz']))

resistanceVect.alignAxisToVect(v,0,1.0)

print("ok")

resistanceVect.localScale = [fighter['resistance']/300000,fighter['resistance']/300000,1]
