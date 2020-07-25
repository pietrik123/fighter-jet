import bge

print("***Target mark ***")

mainScene = bge.logic.getSceneList()[0]

currentScene = bge.logic.getCurrentScene()

targetMark = currentScene.objects['TargetMark']

camera = mainScene.active_camera

fighter = mainScene.objects['FighterJet']

camLimitX = 6
camLimitY = 3.4

if fighter['target'] != None:
	pos = camera.getScreenPosition(fighter['target'])
	
	x = pos[0]*2*camLimitX - camLimitX
	y = -pos[1]*2*camLimitY + camLimitY
	
	targetMark.worldPosition = [y,-x,0]
	
if fighter['target'] == None:
	targetMark.visible = False
else:
	targetMark.visible = True