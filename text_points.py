import bge

owner = bge.logic.getCurrentController().owner

mainScene = bge.logic.getSceneList()[0]

try:	
	owner.text = str(mainScene.objects['Main']['player'].points)
	
except:
	print("Error in displaying player points!")