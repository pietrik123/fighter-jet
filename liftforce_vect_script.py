import bge
import mathutils

cont = bge.logic.getCurrentController()

liftForceVect = cont.owner

scene = bge.logic.getCurrentScene()

fighter = scene.objects['FighterJet']

liftForceVect.worldPosition = fighter.worldPosition

v = fighter['liftVect']

liftForceVect.alignAxisToVect(v,0,1.0)


liftForceVect.localScale = [fighter['lift']/300000,fighter['lift']/300000,1]

