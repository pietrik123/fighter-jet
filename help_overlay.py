import bge

print("***Help overlay script ***")

owner = bge.logic.getCurrentController().owner
scene = bge.logic.getSceneList()[2]

objects = ['Text.001','Text.002','Text.003']

if owner['timer'] < 4:
	for obj in objects:
		scene.objects[obj].visible = True
	
if owner['timer'] > 4:
	for obj in objects:
		scene.objects[obj].visible = False

#bge.logic.endGame()