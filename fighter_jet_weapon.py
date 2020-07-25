import bge
import math
from mathutils import Vector


fighter = bge.logic.getCurrentController().owner
scene = bge.logic.getCurrentScene()

hudScene = bge.logic.getSceneList()[1]

if 'initWeapon' not in fighter:
    fighter['initWeapon'] = True
    fighter['missileLock'] = False

#find target

if 'target' not in fighter:
    fighter['target'] = None
    fighter['targetLocked'] = False
    
    fighter['reloadingPhase'] = 100
    fighter['reloadingFlare'] = 75
    
maxTargetDistance = 3000.0
maxAngle = 40.0

currentTarget = -1
closestIndex = -1
closestDistance = 1000000.0

print("*************Fighter weapon************",bge.logic.getMaxPhysicsFrame())

targets = []

for obj in scene.objects:
    if 'targetProp' in obj:
        targets.append(obj)
        
for i in range(0,len(targets)):
    currentDistance = targets[i].getDistanceTo(fighter)
    
    x = targets[i].worldPosition[0]  - fighter.worldPosition[0]
    y = targets[i].worldPosition[1]  - fighter.worldPosition[1]
    z = targets[i].worldPosition[2]  - fighter.worldPosition[2]
    
    distanceVect = Vector((x,y,z))
    
    angle = math.degrees(distanceVect.angle(fighter.getAxisVect(Vector((1.0,0.0,0.0)))))
    
    if currentDistance < maxTargetDistance and angle < maxAngle:
        if currentDistance < closestDistance:
            closestDistance = currentDistance
            closestIndex = i

if fighter['targetLocked'] == False and closestIndex >= 0:
    fighter['target'] = targets[closestIndex]
    fighter['targetLocked'] = True
    
if fighter['target'] != None:
    
    print(type(fighter['target']))

    x = fighter['target'].worldPosition[0]  - fighter.worldPosition[0]
    y = fighter['target'].worldPosition[1]  - fighter.worldPosition[1]
    z = fighter['target'].worldPosition[2]  - fighter.worldPosition[2]
    
    distanceVect = Vector((x,y,z))
    
    angle = math.degrees(distanceVect.angle(fighter.getAxisVect(Vector((1.0,0.0,0.0)))))

    if fighter['target'].getDistanceTo(fighter) > maxTargetDistance or angle > maxAngle:
        fighter['target'] = None
        fighter['targetLocked'] = False   
else:   
    pass
    
#shoot
if fighter['target'] != None:
    if bge.logic.keyboard.events[bge.events.SPACEKEY] == bge.logic.KX_INPUT_ACTIVE and fighter['reloadingPhase'] == 100: 
        positionObject = scene.objects['missileAddPosition']
        missile = scene.addObject('missile',positionObject,200)

        missile.worldOrientation = fighter.worldOrientation
        missile.setLinearVelocity(Vector((200.0,0.0,0.0)),True)
        missile['target'] = fighter['target']
        fighter['reloadingPhase'] = 0
        
        print('Target set!')

if fighter['reloadingPhase'] < 100:
    fighter['reloadingPhase'] += 1

#flares
if bge.logic.keyboard.events[bge.events.FKEY] == bge.logic.KX_INPUT_ACTIVE:
    if fighter['reloadingFlare'] == 100:
        #release Flare
        positionObject = scene.objects['missileAddPosition']
        flare = scene.addObject('Flare',positionObject,200)

        fighter['reloadingFlare'] = 0
        pass

if fighter['reloadingFlare'] < 100:
    fighter['reloadingFlare'] += 1  

print("****************")
    
# enemy missile radar
warning = False
for obj in scene.objects:  
    if 'enemyMissile' in obj:
        if obj.getDistanceTo(fighter) < 1500 and obj['target'] == fighter:
           warning = True
           break
    
fighter['missileLock'] = warning       