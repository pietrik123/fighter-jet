import bge

scene = bge.logic.getCurrentScene()
camera1 = scene.cameras['Camera.006']
camera2 = scene.cameras['Camera2']

if bge.logic.keyboard.events[bge.events.CKEY] == bge.logic.KX_INPUT_ACTIVE:
    scene.active_camera = camera2
else:
    scene.active_camera = camera1 