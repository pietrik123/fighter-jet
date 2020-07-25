import bge
from mathutils import Vector,Matrix
import math

owner = bge.logic.getCurrentController().owner

if 'size' not in owner:
	owner['size'] = 4.0
else:
	if 'phase' not in owner:
		owner['phase'] = 0
	else:
		phase = owner['phase']
		positionVect = Vector( (owner.worldPosition[0],\
			owner.worldPosition[1],\
			owner.worldPosition[2]))
			
		positionUnitVect = positionVect.normalized()
		scene = bge.logic.getCurrentScene()
		
		if phase == 0:
			scene.addObject('Spark',owner,20)
            
		if phase == 5:	
			newPos = [0,0,0]
			newPosVect = positionVect + positionUnitVect * 3*owner['size']
			
			spark = scene.addObject('Spark',owner,20)
			spark['size'] = owner['size']
			
			spark.worldPosition = newPosVect
					
		if phase == 10:
			newPosVect = positionVect + Matrix.Rotation(math.radians(120.0), 3, 'Z')*3*owner['size']*positionUnitVect
			spark = scene.addObject('Spark',owner,20)
			
			spark['size'] = owner['size']
			spark.worldPosition = newPosVect
			
		if phase == 15:
			newPosVect = positionVect + Matrix.Rotation(math.radians(-120.0), 3, 'Z')*3*owner['size']*positionUnitVect
			spark = scene.addObject('Spark',owner,20)
			
			spark['size'] = owner['size']
			spark.worldPosition = newPosVect
			
		owner['phase'] += 1
			