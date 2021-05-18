# setup blender


import bpy


# preinstalled addons to activate
ACTIVATE_ADDONS = ['add_mesh_extra_objects',
                    'io_scene_fbx',
                    'space_view3d_modifier_tools',
                    'mesh_tools',
                    'mesh_f2',
                    'mesh_looptools',
                    'mesh_tiny_cad',
                    ]  # addons: curve tools, simplify curves+, modifier tools



def setupBlender():
    print ('setting up blender...')
    # blender startup file set:
    
    # activate addons
    for addon in ACTIVATE_ADDONS:
        bpy.ops.preferences.addon_enable(module=addon)
        pass

    # setup preferences and shortcuts
    # https://docs.blender.org/api/current/bpy.types.PreferencesView.html
    # https://docs.blender.org/api/current/bpy.types.PreferencesSystem.html
    # https://docs.blender.org/api/current/bpy.types.PreferencesKeymap.html
    # https://docs.blender.org/api/current/bpy.types.PreferencesInput.html
    # etc https://docs.blender.org/api/current/bpy.types.html

    prefs = bpy.context.preferences
    prefs.view.color_picker_type = 'CIRCLE_HSV' # color picker type
    prefs.view.lookdev_sphere_size = 50 # smaller HDRI spheres
    prefs.view.show_developer_ui = True # enable Developer Extras
    prefs.view.show_splash = False # disable splash screen
    prefs.view.show_statusbar_memory = True
    prefs.view.show_statusbar_stats = True
    prefs.view.show_statusbar_version = True
    prefs.view.show_statusbar_vram = True
    prefs.view.show_tooltips_python = True    # enable python tooltips
    # allow negative frames
    # play button swap with tool button 
    # render_keep user interface
    # color: standard
    # reset 3d cursor
    
    # setup default scene
        # set cycles mode to GPU
        # delete objects
        # enable absolute grid snap
        # remove navigation gizmo, relationship lines from all tabs
        # remove stuff from shading view
        # set grease pencil strength/weight
        # add full screen view
        # set outliner filters
    
    

    print('Done!')




setupBlender()