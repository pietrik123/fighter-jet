import bge
import mathutils

cont = bge.logic.getCurrentController()

thrustForceVect = cont.owner

scene = bge.logic.getCurrentScene()

fighter = scene.objects['FighterJet']

thrustForceVect.worldPosition = fighter.worldPosition

x = fighter.getAxisVect(mathutils.Vector((1.0,0.0,0.0)))

thrustForceVect.alignAxisToVect(x,0,1.0)

thrustForceVect.localScale = [fighter['thrust']/300000,fighter['thrust']/300000,1]
