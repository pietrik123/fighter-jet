import bge

class Player:
	def __init__(self):
		self.points = 0

owner = bge.logic.getCurrentController().owner
scene = bge.logic.getCurrentScene()

print("***Game control script***")

enemies = ['Jet','Jet.001','Jet.002','Jet.003','Jet.004','Truck','truck2','EnemyShip']

if 'initGame' not in owner:
	owner['initGame'] = True
	owner['player'] = Player()

	owner['enemiesPrevState'] = []
	for i in range(0,len(enemies)):
		owner['enemiesPrevState'].append(False)

	for obj in scene.objects:
		obj['reflectRays'] = True
	
else:   	
	for i in range(0,len(enemies)):
		print(enemies[i])
		enemy = scene.objects[enemies[i]]
		print(enemy['hitByMissile'])
		
		if enemy['hitByMissile'] == True and owner['enemiesPrevState'][i]== False:
			
			owner['player'].points += 1
			owner['enemiesPrevState'][i] = enemy['hitByMissile']

	print(owner['player'].points)
	owner['points'] = owner['player'].points
	

