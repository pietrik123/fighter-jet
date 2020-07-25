import bge

owner = bge.logic.getCurrentController().owner

if 'init' not in owner:
    owner['init'] = True  
    owner['cnt'] = 0   
    owner['warning'] = False

else:
    mainScene = bge.logic.getSceneList()[0]   
    fighter = mainScene.objects['FighterJet']    
    owner['cnt'] += 1
    if owner['cnt'] >= 20:
        owner['cnt'] = 0
    
    visible = False
    owner['warning'] = False
    if fighter['missileLock'] == True:
        owner['warning'] = True
        if owner['cnt'] < 10:
            visible = True
            
    owner.visible = visible
    