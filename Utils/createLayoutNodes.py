import bpy
from math import floor
from mathutils import Vector

# A simple utility for Blender's node editor. Adds labelled Reroute nodes.

# from https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html
# https://wiki.blender.org/wiki/Process/Addons/Guidelines/metainfo
bl_info = {
    "name": "Add Labelled Reroute Nodes",
    "author": "Studio RGL www.rgl.tv",
    "description": "A simple addon that adds right-click options to the node editor menu. These creates labelled reroute nodes for the in/outs of selected nodes. Keep those graphs clean!",
    "blender": (2, 80, 0),
    "location": "Node Editor > Right Click Menu",
    "category": "Node",
    "support":"TESTING"
}


# from https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html
class NODE_OT_add_labelled_reroute_nodes(bpy.types.Operator):
    """Add labelled reroute nodes to the selected nodes'"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "node.add_labelled_reroute_nodes"   # Unique identifier for buttons and menu items to reference.
    bl_label = "Add Labelled Reroute Nodes"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    labelInputs: bpy.props.BoolProperty(default = True)
    labelOutputs: bpy.props.BoolProperty(default = True)

    def snapToGrid(self, value, gridSize):
        return gridSize * floor(value/gridSize)

    def execute(self, context):        # execute() is called when running the operator.
        GRID_SPACING = 20

        # get selected nodes
        selectedNodes = context.selected_nodes
        
        for node in selectedNodes:
            node.select = False  # deselect it
            tree = node.id_data

            # Do the input nodes
            if self.labelInputs:
                nodePorts = node.inputs[:]
            
                inputCounter = 0            

                for nodePort in nodePorts:

                    # check if it's connected to anything - if not we ain't doin nothin
                    inputLink = None
                    for l in tree.links:
                        if l.to_socket == nodePort:
                            # link found
                            inputLink = l
                            break # "highlander rules"...
                    
                    if (nodePort.enabled == False) or (inputLink == None):
                        inputCounter += 1 # increment the counter so stuff lines up properly
                        continue # don't bother with this one, nothing to connect it to

                    newRerouteNode = tree.nodes.new("NodeReroute")  # add new reroute node

                    # label it
                    label = inputLink.from_node.label + ' ' + inputLink.from_socket.name
                    newRerouteNode.label = label

                    # figure out position
                    x = node.location.x
                    y = node.location.y

                    x -= GRID_SPACING * 4
                    y -= inputCounter * GRID_SPACING
                    inputCounter += 1
                    
                    snappedX = self.snapToGrid(x, GRID_SPACING)  # snap
                    snappedY = self.snapToGrid(y, GRID_SPACING)  # snap
                    newRerouteNode.location = Vector((snappedX, snappedY))  # position it
                    
                    tree.links.new(inputLink.from_socket, newRerouteNode.inputs[0])  # relink it
                    tree.links.new(newRerouteNode.outputs[0], inputLink.to_socket)  # relink it
                    if inputLink in tree.links[:]:
                        tree.links.remove(inputLink) # think this should be removed automatically so this is gonna be superfluous in most cases

            # Do the output nodes
            if self.labelOutputs:
                # hack to make it align properly.
                # Won't work for fancy GUI nodes like Vector Curves, but should work for reroutes and standard nodes
                if node.type == 'REROUTE':
                    outputCounter = 0
                else:
                    outputCounter = 3
                
                nodePorts = node.outputs[:]
                for nodePort in nodePorts:

                    # skip hidden ports
                    if nodePort.enabled == False:
                        outputCounter += 1
                        continue

                    newRerouteNode = tree.nodes.new("NodeReroute")  # add new reroute node

                    # label it
                    if node.type == 'REROUTE':
                        label = node.label
                    else:
                        label = node.label + ' ' + nodePort.name
                    newRerouteNode.label = label

                    # figure out position
                    x = node.location.x
                    y = node.location.y

                    x += node.width +  GRID_SPACING * 4
                    y -= outputCounter * GRID_SPACING
                    outputCounter += 1
                    
                    snappedX = self.snapToGrid(x, GRID_SPACING)  # snap
                    snappedY = self.snapToGrid(y, GRID_SPACING)  # snap
                    newRerouteNode.location = Vector((snappedX, snappedY))  # position it
                    
                    tree.links.new(nodePort, newRerouteNode.inputs[0])  # link it"""
    
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

