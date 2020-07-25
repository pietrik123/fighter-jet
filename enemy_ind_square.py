# script for showing enemies as small squares on a radar
import bge 

print("***EnemyIndSquare****\nstart")

mainScene = bge.logic.getSceneList()[0]

fighter = mainScene.objects['FighterJet']

activeScene = bge.logic.getCurrentScene()

camera = mainScene.active_camera

enemies = ['Jet','Jet.001','Jet.002','Jet.003','Jet.004','EnemyShip','truck2','Truck']

enemyIndSquares = ['EnemyInd','EnemyInd.001','EnemyInd.002','EnemyInd.003','EnemyInd.004','EnemyInd.005','EnemyInd.006','EnemyInd.007']

enemyMissiles = ['EnemyMissile', 'EnemyMissile.001', 'EnemyMissile.002']

enemyMissileIndCircles = ['EnemyMissileInd','EnemyMissileInd.001','EnemyMissileInd.002']

camLimitX = 6
camLimitY = 3.4

for i in range(0,len(enemies)):
	enemy = mainScene.objects[enemies[i]]
	ind = activeScene.objects[enemyIndSquares[i]]
	pos = camera.getScreenPosition(enemy)
	
	x = pos[0]*2*camLimitX - camLimitX
	y = -pos[1]*2*camLimitY + camLimitY
	
	if (x > camLimitX):
		x = camLimitX
	
	if (x < -camLimitX):
		x = -camLimitX
	
	if (y > camLimitY):
		y = camLimitY
	
	if (y < -camLimitY):
		y = -camLimitY
		
	ind.worldPosition = [y,-x,0]
	if 'destroyed' in enemy:
		ind.visible = False
	
	if 'hitByMissile' in enemy:
		if enemy['hitByMissile'] == True:
			ind.visible = False

for i in range(0,len(enemyMissiles)):
	enemyMissile = mainScene.objects[enemyMissiles[i]]
	ind2 = activeScene.objects[enemyMissileIndCircles[i]]
	pos = camera.getScreenPosition(enemyMissile)
	
	x = pos[0]*2*camLimitX - camLimitX
	y = -pos[1]*2*camLimitY + camLimitY
	
	if (x > camLimitX):
		x = camLimitX
	
	if (x < -camLimitX):
		x = -camLimitX
	
	if (y > camLimitY):
		y = camLimitY
	
	if (y < -camLimitY):
		y = -camLimitY
		
	ind2.worldPosition = [y,-x,0]
	if 'destroyed' in enemyMissile or enemyMissile.getDistanceTo(fighter) > 700.0:
		ind2.visible = False
	else:
		ind2.visible = True