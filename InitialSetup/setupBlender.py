# setup blender

import bpy


# preinstalled addons to activate
ACTIVATE_ADDONS = []



def setupBlender():
    print ('setting up blender...')
    # blender startup file set:
    # 
    # set cycles mode to GPU
    # delete objects
    # color: standard
    # remove navigation gizmo, relationship lines from all tabs
    # render_keep user interface
    # reset 3d cursor
    # remove stuff from shading view
    # set outliner filters
    # add full screen view
    # play button swap with tool button 
    # set grease pencil strength/weight
    # enable Developer Extras
    # disable splash screen
    # enable python tooltips
    # allow negative frames
    # enable absolute grid snap
    # 
    
    
    # addons: curve tools, simplify curves+, modifier tools
    for addon in ACTIVATE_ADDONS:
        #bpy.ops.preferences.addon_enable(module='')
        pass

    print('Done!')




setupBlender()