import bpy


# from https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html
# https://wiki.blender.org/wiki/Process/Addons/Guidelines/metainfo
bl_info = {
    "name": "Add Labelled Reroute Nodes",
    "author": "Studio RGL www.rgl.tv",
    "description": "A simple addon that adds a right-click option to the node editor menu, 'Add Labelled Reroute Nodes'. This creates labelled reroute nodes for every output of the selected nodes. Keep those graphs clean!",
    "blender": (2, 80, 0),
    "location": "Node Editor > Right Click Menu",
    "category": "Node",
}

# from https://blender.stackexchange.com/questions/150101/python-how-to-add-items-in-context-menu-in-2-8
def draw_menu(self, context):
    layout = self.layout
    layout.separator()
    layout.operator("node.duplicate_move", text="Add Labelled Reroute Nodes")


def register():
    print("Activating addon")
    bpy.types.NODE_MT_context_menu.append(draw_menu)


def unregister():
    print("Deactivating addon")
    bpy.types.NODE_MT_context_menu.remove(draw_menu)


# create a labelled layout node for each pin on a node
def createLabelledReroutes():
    
    pass 