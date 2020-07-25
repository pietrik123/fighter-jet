import bge

owner = bge.logic.getCurrentController().owner

if 'size' not in owner:
	pass
else:
	if 'phase' not in owner:
		owner['phase'] = 0.0
	factor = owner['size']*owner['phase']/7.0 + 1.0
	owner.localScale = [factor,factor,factor]
	
	owner['phase'] += 1