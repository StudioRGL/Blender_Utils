import bpy


# from https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html
# https://wiki.blender.org/wiki/Process/Addons/Guidelines/metainfo
bl_info = {
    "name": "Add Labelled Reroutes",
    "author": "Studio RGL www.rgl.tv",
    "description": "A simple addon that adds a right-click option to the node editor menu, 'Add Labelled Reroutes'. This creates labelled reroute nodes for every output of the selected nodes. Keep those node graphs clean!",
    "blender": (2, 80, 0),
    "location": "Node Editor > Right Click Menu",
    "category": "Node",
}

def register():
    print("Hello World")

def unregister():
    print("Goodbye World")


# create a labelled layout node for each pin on a node
def createLabelledReroutes():
    
    pass 