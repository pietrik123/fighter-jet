import bge

bomb = bge.logic.getCurrentController().owner
scene = bge.logic.getCurrentScene()

print("***bomb script***")
if bomb.worldPosition[2] < 10.0 and 'exploded' not in bomb:
	scene.addObject('Explosion',bomb,100)
	print("ok")