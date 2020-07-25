import bge
import math
import mathutils

flare = bge.logic.getCurrentController().owner

if 'init' not in flare:
	flare['phase'] = 0.0
	flare['init'] = True

value = 1.0*math.sin(flare['phase']) + 0.5	

flare.localScale = mathutils.Vector((value,value,value))

flare['phase'] += 0.1