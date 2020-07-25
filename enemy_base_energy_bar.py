import bge

owner = bge.logic.getCurrentController().owner

mainScene = bge.logic.getSceneList()[0]

currentScene = bge.logic.getCurrentScene()

bar = currentScene.objects['EnemyBaseEnergyBar']

base = mainScene.objects['EnemyBaseCenter']

fighter = mainScene.objects['FighterJet']

bar.worldScale = [1,base['energy']/100.0,1]

camLimitX = 6
camLimitY = 3.4

camera = mainScene.active_camera
	
pos = camera.getScreenPosition(base)
	
x = pos[0]*2*camLimitX - camLimitX
y = -pos[1]*2*camLimitY + camLimitY

if base.getDistanceTo(fighter) < 1000.0:
	bar.worldPosition = [y,-x,0]
else:
	bar.worldPosition = [-500,-500,0]