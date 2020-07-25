import bge
import math

fighter = bge.logic.getCurrentController().owner
soundAct = fighter.actuators['Sound']

if fighter['destroyed'] == False:
    volume = 0.0000025*math.fabs(fighter['thrust']) + 0.1
  
    soundAct.volume = volume
else:
    soundAct.volume = 0.0
    