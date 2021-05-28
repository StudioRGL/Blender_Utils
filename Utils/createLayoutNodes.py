import bpy
from math import floor
from mathutils import Vector


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


# from https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html
class NODE_OT_add_labelled_reroute_nodes(bpy.types.Operator):
    """Add labelled reroute nodes to all the selected nodes' outputs"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "node.add_labelled_reroute_nodes"   # Unique identifier for buttons and menu items to reference.
    bl_label = "Add Labelled Reroute Nodes"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def snapToGrid(self, value, gridSize):
        return gridSize * floor(value/gridSize)

    def execute(self, context, labelInputs = False, labelOutputs = True):        # execute() is called when running the operator.
        GRID_SPACING = 20

        # get selected nodes
        selectedNodes = context.selected_nodes
        
        for node in selectedNodes:
            node.select = False  # deselect it
            tree = node.id_data
            counter = 0

            # snap to grid
            x = self.snapToGrid(node.location.x + node.width, GRID_SPACING)
            y = self.snapToGrid(node.location.y, GRID_SPACING)
            snappedNodeLocation = Vector((x,y))
            
            nodePorts = []
            if labelInputs:
                nodePorts += node.inputs[:]
            if labelOutputs:
                nodePorts += node.outputs[:]
            

            for output in node.outputs:
                # print(output.name)
                newRerouteNode = tree.nodes.new("NodeReroute")  # add new reroute node

                # label it
                if node.type == 'REROUTE':
                    label = node.label
                else:
                    label = node.label + ' ' + output.name
                newRerouteNode.label = label

                newRerouteNode.location = snappedNodeLocation + Vector(( GRID_SPACING*4, counter*-GRID_SPACING*2))  # position it
                tree.links.new(output, newRerouteNode.inputs[0])  # link it
                
                counter += 1 # increment position counter

        
        return {'FINISHED'}            # Lets Blender know the operator finished successfully.


# from https://blender.stackexchange.com/questions/150101/python-how-to-add-items-in-context-menu-in-2-8
def draw_menu(self, context):
    """Add the operator to the right-click menu"""
    layout = self.layout
    layout.separator()
    # layout.operator("node.duplicate_move", text="Add Labelled Reroute Nodes")
    layout.operator("node.add_labelled_reroute_nodes", text="Add Labelled Reroute Nodes") 


def register():
    print("Activating addon")
    bpy.utils.register_class(NODE_OT_add_labelled_reroute_nodes)  # register the operator
    bpy.types.NODE_MT_context_menu.append(draw_menu)  # add it to the menu


def unregister():
    print("Deactivating addon")
    bpy.utils.unregister_class(NODE_OT_add_labelled_reroute_nodes)  # unregister
    bpy.types.NODE_MT_context_menu.remove(draw_menu) # remove it from the menu
