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

    labelInputs: bpy.props.BoolProperty(default = True)
    labelOutputs: bpy.props.BoolProperty(default = True)

    def snapToGrid(self, value, gridSize):
        return gridSize * floor(value/gridSize)

    def execute(self, context):        # execute() is called when running the operator.
        print ('Executing...')
        GRID_SPACING = 20

        # get selected nodes
        selectedNodes = context.selected_nodes
        
        for node in selectedNodes:
            node.select = False  # deselect it
            tree = node.id_data
            inputCounter = 0
            outputCounter = 0


            
            nodePorts = []
            if self.labelInputs:
                nodePorts += node.inputs[:]
            if self.labelOutputs:
                nodePorts += node.outputs[:]
            
            for nodePort in nodePorts:
                newRerouteNode = tree.nodes.new("NodeReroute")  # add new reroute node

                # check if the node's an input node, we'll use this throughout
                if nodePort in node.inputs[:]:
                    nodeIsInput = True
                else:
                    nodeIsInput = False  # there's probably a cooler way of doing this but hey
                
                # label it
                if nodeIsInput:
                    label = 'input'
                else:
                    # it's an output
                    if node.type == 'REROUTE':
                        label = node.label
                    else:
                        label = node.label + ' ' + nodePort.name
                newRerouteNode.label = label

                # figure out position
                x = node.location.x
                y = node.location.y

                if nodeIsInput:
                    x -= GRID_SPACING * 4
                    y -= inputCounter * GRID_SPACING
                    inputCounter += 1
                else: # it's an output
                    x += node.width +  GRID_SPACING * 4
                    y -= outputCounter * GRID_SPACING
                    outputCounter += 1
                
                
                snappedX = self.snapToGrid(x, GRID_SPACING)  # snap
                snappedY = self.snapToGrid(y, GRID_SPACING)  # snap
                newRerouteNode.location = Vector((snappedX, snappedY))  # position it
                
                if nodeIsInput:
                    pass
                    # find the link that ends in this port [highlander rules!]
                    # change the end link to conect to the new reroute
                    # add a new link after the reroute
                else:
                    tree.links.new(nodePort, newRerouteNode.inputs[0])  # link it
                
        
    
        return {'FINISHED'}            # Lets Blender know the operator finished successfully.
    
    
    #def invoke(self, context, labelInputs, labelOutputs):
    #    self.labelInputs = labelInputs
    #    self.labelOutputs = labelOutputs
    #    self.execute(context)

# from https://blender.stackexchange.com/questions/150101/python-how-to-add-items-in-context-menu-in-2-8
def draw_menu(self, context):
    """Add the operator to the right-click menu"""
    layout = self.layout
    layout.separator()
    
    newOperator = layout.operator("node.add_labelled_reroute_nodes", icon='TRIA_LEFT', text="Add Labelled Inputs")  # https://docs.blender.org/api/current/bpy.types.UILayout.html
    newOperator.labelInputs = True
    newOperator.labelOutputs = False
    newOperator = layout.operator("node.add_labelled_reroute_nodes", icon='TRIA_RIGHT', text="Add Labelled Outputs")  # https://docs.blender.org/api/current/bpy.types.UILayout.html
    newOperator.labelInputs = False
    newOperator.labelOutputs = True
    



def register():
    print("Activating addon")
    bpy.utils.register_class(NODE_OT_add_labelled_reroute_nodes)  # register the operator
    bpy.types.NODE_MT_context_menu.append(draw_menu)  # add it to the menu


def unregister():
    print("Deactivating addon")
    bpy.utils.unregister_class(NODE_OT_add_labelled_reroute_nodes)  # unregister
    bpy.types.NODE_MT_context_menu.remove(draw_menu) # remove it from the menu

