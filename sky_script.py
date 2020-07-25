import bge

owner = bge.logic.getCurrentController().owner

scene = bge.logic.getCurrentScene()

fighter = scene.objects['FighterJet']

owner.worldPosition = fighter.worldPosition
owner.worldPosition[2] = 0.0