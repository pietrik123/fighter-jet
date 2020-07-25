import bge
from mathutils import *

fighter = bge.logic.getCurrentController().owner
scene = bge.logic.getCurrentScene()

elevatorLeft = scene.objects['ElevatorLeft']
elevatorRight = scene.objects['ElevatorRight']
rudderLeft = scene.objects['RudderLeft']
rudderRight = scene.objects['RudderRight']
aileronLeft = scene.objects['AileronLeft']
aileronRight = scene.objects['AileronRight']

if 'steeringElementsInit' not in fighter:
    fighter['aileronLeftAngle'] = 0.0
    fighter['aileronRightAngle'] = 0.0
    fighter['rudderLeftAngle'] = 0.0
    fighter['rudderRightAngle'] = 0.0
    fighter['elevatorAngle'] = 0.0
    
    fighter['steeringElementsInit'] = True
    
else:
    if bge.logic.keyboard.events[bge.events.DOWNARROWKEY] == bge.logic.KX_INPUT_ACTIVE:
        fighter['elevatorAngle'] += 0.05 
              
        if fighter['elevatorAngle'] > 0.50:
            fighter['elevatorAngle'] = 0.5
        else:
            elevatorLeft.applyRotation(Vector((0.0,0.05,0.0)),True)     
            elevatorRight.applyRotation(Vector((0.0,0.05,0.0)),True)        
           
    if bge.logic.keyboard.events[bge.events.UPARROWKEY] == bge.logic.KX_INPUT_ACTIVE:
        fighter['elevatorAngle'] -= 0.05 
    
        if fighter['elevatorAngle'] < -0.50:
            fighter['elevatorAngle'] = -0.5
        else:
            elevatorLeft.applyRotation(Vector((0.0,-0.05,0.0)),True)        
            elevatorRight.applyRotation(Vector((0.0,-0.05,0.0)),True)
    
    print("Steering elements script!")   
    print("************")
       
    if bge.logic.keyboard.events[bge.events.DOWNARROWKEY] == bge.logic.KX_INPUT_NONE and bge.logic.keyboard.events[bge.events.UPARROWKEY] == bge.logic.KX_INPUT_NONE:
        if fighter['elevatorAngle'] < 0.0:
            fighter['elevatorAngle'] += 0.05
            elevatorLeft.applyRotation(Vector((0.0,0.05,0.0)),True)     
            elevatorRight.applyRotation(Vector((0.0,0.05,0.0)),True)   
        if fighter['elevatorAngle'] > 0.0:
            fighter['elevatorAngle'] -= 0.05
            elevatorLeft.applyRotation(Vector((0.0,-0.05,0.0)),True)        
            elevatorRight.applyRotation(Vector((0.0,-0.05,0.0)),True)   

    if bge.logic.keyboard.events[bge.events.LEFTARROWKEY] == bge.logic.KX_INPUT_ACTIVE:
        fighter['aileronLeftAngle'] += 0.05
        fighter['aileronRightAngle'] -= 0.05
        
        if fighter['aileronLeftAngle'] > 0.5:
            fighter['aileronLeftAngle'] = 0.5
            fighter['aileronRightAngle'] = -0.5
        else:
            aileronLeft.applyRotation(Vector((0.0,0.05,0.0)),True)
            aileronRight.applyRotation(Vector((0.0,-0.05,0.0)),True)
            
    if bge.logic.keyboard.events[bge.events.RIGHTARROWKEY] == bge.logic.KX_INPUT_ACTIVE:
        fighter['aileronLeftAngle'] -= 0.05
        fighter['aileronRightAngle'] += 0.05
        
        if fighter['aileronLeftAngle'] < -0.5:
            fighter['aileronLeftAngle'] = -0.5
            fighter['aileronRightAngle'] = 0.5
            
        else:
            aileronLeft.applyRotation(Vector((0.0,-0.05,0.0)),True)
            aileronRight.applyRotation(Vector((0.0,0.05,0.0)),True)
            
    if bge.logic.keyboard.events[bge.events.LEFTARROWKEY] == bge.logic.KX_INPUT_NONE and bge.logic.keyboard.events[bge.events.RIGHTARROWKEY] == bge.logic.KX_INPUT_NONE:
        if fighter['aileronLeftAngle'] > 0.0:
            fighter['aileronLeftAngle'] -= 0.05
            fighter['aileronRightAngle'] += 0.05
            aileronLeft.applyRotation(Vector((0.0,-0.05,0.0)),True)
            aileronRight.applyRotation(Vector((0.0,+0.05,0.0)),True)
                     
        if fighter['aileronLeftAngle'] < 0.0:
            fighter['aileronLeftAngle'] += 0.05
            fighter['aileronRightAngle'] -= 0.05
            aileronLeft.applyRotation(Vector((0.0,0.05,0.0)),True)
            aileronRight.applyRotation(Vector((0.0,-0.05,0.0)),True)
             