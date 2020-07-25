import bge

import mathutils

cont = bge.logic.getCurrentController()

velocityVect = cont.owner

scene = bge.logic.getCurrentScene()

fighter = scene.objects['FighterJet']

#camera position
velocityVect.worldPosition = fighter.worldPosition

v = mathutils.Vector((fighter['vx'],fighter['vy'],fighter['vz']))

velocityVect.alignAxisToVect(v,0,1.0)

velocityVect.localScale = [fighter['speed']/100,fighter['speed']/100,1]
