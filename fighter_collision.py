import mathutils
fighter = bge.logic.getCurrentController().owner

fighterSpeed = fighter.getLinearVelocity(False)

fighterSpeedXY = mathutils.Vector((fighterSpeed[0],fighterSpeed[1],0.0))
   
if fighter['destroyed'] == True:
    
    resitance = fighterSpeedXY.length * 3000
    fighter.applyForce((-resitance)*fighterSpeedXY.normalized())
    
print("********Friction scrtipt*****")
print(resitance*fighterSpeedXY.normalized())
print("*****************************")
    