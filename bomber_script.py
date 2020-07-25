import bge
import mathutils

bomber = bge.logic.getCurrentController().owner
scene = bge.logic.getCurrentScene()

print("***Bomber script***")

#init
if 'init' not in bomber:
	
	
	bomber['i'] = 0
	bomber['startTimeSet'] = False
	bomber['startTime'] = 0
	bomber['init'] = True
	
	bomber['file'] = open('log_figher.txt','w')

file = bomber['file']
file.write('step 1 ok\n')
loc = mathutils.Vector((487,-48,51))
numOfBombs = 10
i = bomber['i']
timer = bomber['timer']
startTimeSet = bomber['startTimeSet']
startTime = bomber['startTime']
file.write('step 2 ok\n')

if bomber.getDistanceTo(loc) < 100 and startTimeSet == False:
	bomber['startTime'] = timer
	bomber['startTimeSet'] = True
	file.write("start time set\n") 

if startTimeSet == True and timer > (startTime + i*2):
	scene.addObject('Bomb','B2_bomber',200)
	bomber['i'] += 1
	print("bomb dropped")
	file.write("bomb dropped\n")
	

