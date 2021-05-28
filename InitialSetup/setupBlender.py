# setup blender

# TODO: add
# CyclesPreferences.compute_device_type
# SWAP KEYFRAME KEYS! up vs down
# set noodles to curvy
# 

import bpy


# preinstalled addons to activate
ACTIVATE_ADDONS = ['add_mesh_extra_objects',
                    'io_scene_fbx',
                    'space_view3d_modifier_tools',
                    'mesh_tools',
                    'mesh_f2',
                    'mesh_looptools',
                    'mesh_tiny_cad',
                    'rigify'
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
    # etc https://docs.blender.org/api/current/bpy.types.Preferences.html

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
    prefs.view.render_display_type = 'NONE' # render_keep user interface

    prefs.edit.use_negative_frames = True # allow negative frames
    prefs.edit.undo_steps = 80
    
    # sequencer
    prefs.system.memory_cache_limit = 8192
    prefs.system.use_sequencer_disk_cache = True
    prefs.system.sequencer_disk_cache_dir = "D:/Temp/blender/sequencerDiskCache/"
    prefs.system.sequencer_disk_cache_compression = 'HIGH'

    activeKeyConfig = prefs.keymap.active_keyconfig
    bpy.context.window_manager.keyconfigs[activeKeyConfig].preferences.spacebar_item = 'TOOL'    # play button swap with tool button https://blender.stackexchange.com/questions/184422/how-to-access-the-kemap-settings-preferences-spacebar-action-select-mouse-butt

    
    
    # setup default scene
    
    
    for screen in bpy.data.screens:
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                s  = area.spaces[0]
                s.show_gizmo_navigate = False # remove navigation gizmo, relationship lines from all tabs 
                s.overlay.show_relationship_lines = False
                s.show_region_toolbar = False
                s.overlay.show_look_dev = False # remove stuff from shading view

            elif area.type == 'OUTLINER':
                # set outliner filters
                s  = area.spaces[0]
                s.show_restrict_column_render = True
                s.show_restrict_column_holdout = True
                s.show_restrict_column_select = True
                s.show_restrict_column_viewport = True


    bpy.context.scene.cycles.device = 'GPU' # set cycles mode to GPU
    bpy.ops.object.select_all(action = 'SELECT') # select all
    bpy.ops.object.delete(use_global=False, confirm=False) # delete objects
    bpy.context.scene.tool_settings.use_snap_grid_absolute = True  # enable absolute grid snap
    bpy.data.brushes["Pencil"].tool_settings.gpencil_paint.brush.gpencil_settings.pen_strength = 1 # set grease pencil strength/weight
    
    # add full screen view
    bpy.ops.workspace.duplicate()
    bpy.context.workspace.name = 'Fullscreen'

    #for a in C.workspace.screens[0].areas[1:]:

    
    bpy.ops.wm.save_homefile() # save new default file
    

    print('Done!')




setupBlender()