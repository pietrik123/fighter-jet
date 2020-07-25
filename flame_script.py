import bge
import math
import mathutils

cont = bge.logic.getCurrentController()

owner = cont.owner

if 'angle' not in owner:
	owner['angle'] = 0.0
	
owner['angle'] += 1.4;

scale_value = 1.0 + math.sin(owner['angle'])/11.0

owner.localScale = mathutils.Vector((scale_value,scale_value,scale_value))

print(scale_value)