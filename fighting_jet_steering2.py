#import section
import bge
from mathutils import *
import math

#Function returns lift coeficient depending 
# on angle of attack of an aircraft and speed and also altitude.
# angleOfAttack [deg], speed [m/s]
# returned value [no unit]
def getLiftCoef(angleOfAttack,speed): 
	coef = 0;
	if angleOfAttack >= -5 and angleOfAttack < 20:
		coef = angleOfAttack*0.1 + 0.5
	elif angleOfAttack >= 20 and angleOfAttack < 25:
		coef = -angleOfAttack*0.1 + 4
	elif angleOfAttack >= 25 and angleOfAttack < 50:
		coef = 1.5
	elif angleOfAttack > 50 and angleOfAttack < 90:
		coef = -angleOfAttack*0.07 + 6.5
		
	if fighter.worldPosition[2] > 600.0:
		coef = 0.0

	return coef

#Function returns value of lift force depending on speed and angle of attack.
# speed [m/s], angleOfAttack [deg]
# returned value [N]
#
def getLiftForceValue(speed,angleOfAttack):
	limit = 1.2*300000.0	
	#70.0 [m^2] wing area
	#1.22 [kg*m^-3] air density	
	liftForceValue = getLiftCoef(angleOfAttack,speed)*(speed**2.0)*70.0*1.22*0.5
	
	if liftForceValue > limit:
		liftForceValue = limit

	if fighter['destroyed'] == True:
		liftForceValue *= 0.1
	
	return liftForceValue
	
#Function returns resistance force value. It depends on angle (between fighter's X axis and it's velocity 
# vector) and speed of an aircraft.
# returned value [N]
#
def getResistanceForceValue(fighter):
	xAxis = fighter.getAxisVect(Vector((1.0,0.0,0.0)))
	angle = 0 
	if fighter.getLinearVelocity(False).length > 0.001:
		angle = math.degrees(xAxis.angle(fighter.getLinearVelocity(False))) # [rad]
	else:
		angle = 0
		
	result = ((100)*fighter['speed'])*((angle**1.0)*0.3+1)

	if result > 300000:
		result = 300000
	if fighter.worldPosition[2] > 600.0:
		result *= 3.0
	
	if fighter['destroyed'] == True:
		result *= 5
	return result
	
	#(angle * 0.3 + 1) - additional coeficient, when velocity vector is not aligned to fighter x axis
	#angle in degrees
	
#Function returns angle of attack of an aircraft. It is an angle between aircraft's
# X axis and velocity vector.
# returned value [deg]
#
	
def getAngleOfAttack(fighter):
	#returns angle in degrees
	speedVect = fighter.getLinearVelocity(False)
	fighterXAxisVect = fighter.getAxisVect(Vector((1.0,0.0,0.0)))
	angle = 0
	try:
		angle = math.degrees(speedVect.angle(fighterXAxisVect))
	except:
		angle = 0
	if fighterXAxisVect[2] <= 0:
		angle *= -1
	return angle

print("******Jet Steering*****")
###########
#PARAMS

fighter = bge.logic.getCurrentController().owner
scene = bge.logic.getCurrentScene()
#INIT
if 'init' not in fighter:
	fighter['phase'] = 0
	fighter['init'] = True
	fighter['prevSpeedVect'] = Vector((70.0,0.0,0.0))
	fighter.setLinearVelocity(Vector((70.0,0.0,0.0)),False)

#IF DESTROYED - GFX
if fighter['destroyed'] == True:
	
	if fighter['phase'] < 20:
		explosion = scene.addObject('Explosion',fighter,50)
		explosion['size'] = 8.0
	fighter['phase'] = fighter['phase'] + 1
	print('abc') 

if fighter['destroyed'] == True:
	
	fighter.visible = False
	scene.objects['EngineFlare'].visible = False
	scene.objects['EngineFlare2'].visible = False
	scene.objects['RudderLeft'].visible = False
	scene.objects['RudderRight'].visible = False
	scene.objects['ElevatorLeft'].visible = False
	scene.objects['ElevatorRight'].visible = False
	scene.objects['AileronLeft'].visible = False
	scene.objects['AileronRight'].visible = False
	scene.objects['FighterShadow'].visible = False

#ADDITIONAL  PARAMS
fighter.linVelocityMax = 270.0

mass = 30e3 #[kg]
maxThrustValue = 350e3 #[N]
maxVelocity = 612 #[m/s]
gravAcc = 9.81 #[m/s^2]

thrustForceValue = fighter['thrust']

#############3
#KEYBOARD INPUT

if bge.logic.keyboard.events[bge.events.WKEY] == bge.logic.KX_INPUT_ACTIVE:
	thrustForceValue = thrustForceValue + 30000
	if thrustForceValue > maxThrustValue:
		thrustForceValue = maxThrustValue

if bge.logic.keyboard.events[bge.events.SKEY] == bge.logic.KX_INPUT_ACTIVE:
	thrustForceValue = thrustForceValue - 30000
	if thrustForceValue < -maxThrustValue*4.0:
		thrustForceValue = -maxThrustValue*4.0
		
if fighter['destroyed'] == True:
	thrustForceValue = 0.0  

dalpha_pitch = 0
dalpha_roll = 0

if bge.logic.keyboard.events[bge.events.UPARROWKEY] == bge.logic.KX_INPUT_ACTIVE:
	dalpha_pitch = 0.015

if bge.logic.keyboard.events[bge.events.DOWNARROWKEY] == bge.logic.KX_INPUT_ACTIVE:
	dalpha_pitch = -0.015
	
if bge.logic.keyboard.events[bge.events.LEFTARROWKEY] == bge.logic.KX_INPUT_ACTIVE:
	dalpha_roll = -0.03

if bge.logic.keyboard.events[bge.events.RIGHTARROWKEY] == bge.logic.KX_INPUT_ACTIVE:
	dalpha_roll = 0.03
	
#Not used now
# if bge.logic.keyboard.events[bge.events.OKEY] == bge.logic.KX_INPUT_ACTIVE:
	# if fighter['prevBombCoverOpen'] == 0:
		# fighter['bombCoverOpen'] = 1
	
	# if fighter['prevBombCoverOpen'] == 1:
		# fighter['bombCoverOpen'] = 0
	

	
# if bge.logic.keyboard.events[bge.events.KKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED:
	# if fighter['prevLandingGearOpen'] == 0:
		# fighter['landingGearOpen'] = 1
	
	# if fighter['prevLandingGearOpen'] == 1:
		# fighter['landingGearOpen'] = 0
	
#####################
#####################
#PHYSICS
#####################
#####################

gravityForce  = mass * gravAcc

fighterOrientation = fighter.worldOrientation

fighterVelocity = fighter.getLinearVelocity(False)
fighterVelocityLocal =  fighter.getLinearVelocity(True)

fighterVelocityUnitVect = fighterVelocity.normalized()

liftForceDirectionVect = fighter.getAxisVect(Vector((0.0,0.0,1.0)))

fighter['liftVect'] = liftForceDirectionVect

speed = fighterVelocity.length
fighter['speed'] = speed
angleOfAttack = getAngleOfAttack(fighter)

fighter['liftX'] = liftForceDirectionVect[0]
fighter['liftY'] = liftForceDirectionVect[1]
fighter['liftZ'] = liftForceDirectionVect[2]

liftForceValue = getLiftForceValue(speed,angleOfAttack)
resistanceForceValue = getResistanceForceValue(fighter)

if fighter.worldPosition[2] > 500.0:
	liftForceValue = -liftForceValue*0.3
	
totalForce = \
[ \
fighterOrientation[0][0] * thrustForceValue - fighterVelocityUnitVect[0]*resistanceForceValue + liftForceDirectionVect[0] * liftForceValue,\
fighterOrientation[1][0] * thrustForceValue - fighterVelocityUnitVect[1]*resistanceForceValue + liftForceDirectionVect[1] * liftForceValue,\
fighterOrientation[2][0] * thrustForceValue - fighterVelocityUnitVect[2]*resistanceForceValue + liftForceDirectionVect[2] * liftForceValue\
]


#centrifugal force
centrifugalForce = [0,0,0]
centrifugalForce[0] = liftForceDirectionVect[0]*liftForceValue
centrifugalForce[1] = liftForceDirectionVect[1]*liftForceValue
centrifugalForce[2] = liftForceDirectionVect[2]*liftForceValue - gravityForce

centrifugalForceValue = (centrifugalForce[0]**2 + centrifugalForce[1]**2 + centrifugalForce[2]**2)**0.5

auxVector2 = fighter.getAxisVect(Vector((0.0,1.0,0.0)))
auxVector2[2] = 0.0

#rotation angle around local z axis
fighterSpeedXY = (fighterVelocity[0]**2.0 + fighterVelocity[1]**2.0)**0.5
if fighterSpeedXY > 0.0:
	auxVector = fighter.getAxisVect(Vector((0.0,0.0,1.0)))
	print(auxVector.angle(auxVector2))
	
	print(auxVector)
	
	
	omega = math.cos(auxVector.angle(auxVector2))*getLiftForceValue(speed,angleOfAttack)/fighterVelocityLocal[0]/mass
	
	if (auxVector[2] < 0.0):
		omega = omega * (-1)
else:
	omega = 0.0

#force correction
#print(totalForce)
totalForce[0] = totalForce[0] * 0.001
totalForce[1] = totalForce[1] * 0.001
totalForce[2] = totalForce[2] * 0.001

#DESTRUCTION - sudden change of speed

changeVect = Vector((fighterVelocity.x - fighter['prevSpeedVect'].x,fighterVelocity.y - fighter['prevSpeedVect'].y,fighterVelocity.z - fighter['prevSpeedVect'].z))

if changeVect.length > 30.0:
	fighter['destroyed'] = True

##########
#APPLY MOVEMENT

#check pitch

xAxisNow = fighter.getAxisVect(Vector((1.0,0.0,0.0)))
xAxisAfterPitch = fighter.worldOrientation*Matrix.Rotation(dalpha_pitch,3,'Y')*Vector((1.0,0.0,0.0))

if (xAxisAfterPitch.angle(fighterVelocity) > math.radians(45.0)) and (xAxisAfterPitch.angle(fighterVelocity) > xAxisNow.angle(fighterVelocity)) :	
	dalpha_pitch = dalpha_pitch / 3.0;

if (xAxisAfterPitch.angle(fighterVelocity) > math.radians(60.0)) and (xAxisAfterPitch.angle(fighterVelocity) > xAxisNow.angle(fighterVelocity)) :	
	dalpha_pitch = dalpha_pitch / 10.0;

	
##################

#print("***",fighter.worldOrientation*Matrix.Rotation(dalpha_pitch,3,'X'))
#print("****", dalpha_pitch)
#print("***", xAxisAfterPitch.angle(fighterVelocity))
#print("***", xAxisNow.angle(fighterVelocity))
#slight aligning fighter x axis to velocity vector

alpha = fighterVelocity.angle(fighter.getAxisVect(Vector((1.0,0.0,0.0))))

factor = 0.00174/alpha

if factor < 0.01 and fighter['speed'] > 70.0:
	fighter.alignAxisToVect(fighterVelocity,0,factor)


#aligning velocity to fighter's x axis
velocityVect = bge.logic.getCurrentScene().objects['VelocityVect']

fighterXVect = fighter.getAxisVect(Vector((1.0,0.0,0.0)))

angle = fighterXVect.angle(velocityVect.getAxisVect(Vector((1.0,0.0,0.0)))) 

#if liftForceValue > gravityForce and angle > 0.05 and fighter.getLinearVelocity().length > 100.0:
#   velocityVect.alignAxisToVect(fighterXVect,0,0.03/angle)
#   
#   fighter.setLinearVelocity(velocityVect.getAxisVect(Vector((1.0,0.0,0.0)))*speed)

alignCoef = 0
speedX = fighter.getLinearVelocity(True)[0]
if speedX > 110 and speedX < 150:
   alignCoef = 0.0125 * speedX - 0.0875
elif speedX >= 150:
   alignCoef = 1


if speedX > 70.0 and angle > 0.05:   
   velocityVect.alignAxisToVect(fighterXVect,0,0.05/angle*alignCoef)
   fighter.setLinearVelocity(velocityVect.getAxisVect(Vector((1.0,0.0,0.0)))*speed)
   
################################################	


if fighter['destroyed'] == False:   

	fighter.applyRotation(Vector((dalpha_roll,dalpha_pitch,0)),True)
	fighter.worldAngularVelocity = Vector((0,0,omega))
	fighter.applyForce(Vector((totalForce[0],totalForce[1],totalForce[2])),False)

#OTHER

fighter['prevDestroyed'] = fighter['destroyed']
		
##DEBUG

auxVector3= fighter.getAxisVect(Vector((1.0,0.0,0.0)))
auxVector3[2] = 0.0

fighter['pitch'] = math.degrees(fighter.getAxisVect(Vector((1.0,0.0,0.0))).angle(auxVector3))

fighter['roll'] = math.degrees(fighter.getAxisVect(Vector((0.0,1.0,0.0))).angle(auxVector2))

fighter['speed'] = speed

fighter['thrust'] = thrustForceValue
fighter['lift'] = liftForceValue*liftForceDirectionVect[2]
fighter['resistance'] = resistanceForceValue

fighter['angle'] = angleOfAttack

fighter['alt'] = fighter.worldPosition[2]

fighter['total'] = (totalForce[0]**2.0 + totalForce[0]**2.0 + totalForce[0]**2.0)**0.5 * 1000
fighter['totalx'] = totalForce[0] * 1000
fighter['totaly'] = totalForce[1] * 1000
fighter['totalz'] = totalForce[2] * 1000

fighter['vx'] = fighterVelocity[0]
fighter['vy'] = fighterVelocity[1]
fighter['vz'] = fighterVelocity[2]

fighter['prevSpeedVect'] = fighterVelocity

print("*****Ok*******")

if fighter.getDistanceTo(Vector((-191,19,fighter.worldPosition[2]))) > 7500.0:
	fighter.worldPosition = [-191,19,200.0]
	fighter.setLinearVelocity(Vector((100.0,0.0,0.0)),False)
	fighter['prevSpeedVect'] = fighter.getLinearVelocity(False)
	
	
