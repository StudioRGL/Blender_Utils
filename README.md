# Studio RGL Blender Utils

A few lil' useful things, created for internal use at Studio RGL. If you find them useful, let us know :-)

www.rgl.tv

https://www.instagram.com/realgoodliars/

https://twitter.com/realgoodliars

## *Add_labelled_reroute_nodes* Addon
### Usage
1) Download `Addons/createLayoutNodes.py` (simplest way is just to download the whole repository, or you can go to the file and choose `Raw`
2) Install the .py via Blender Preferences->Add-ons->Install
![image](https://user-images.githubusercontent.com/16046786/119989551-37c13600-bfbf-11eb-93a3-6d4a90514834.png)

3) Activate it (make sure the check box is checked
4) In any node editor, select one or more nodes, then right click and choose either `Add Labelled Inputs` or `Add Labelled Outputs`
![image](https://user-images.githubusercontent.com/16046786/119989325-f29d0400-bfbe-11eb-9670-2dbc7487f643.png)
5) This will create labelled reroute nodes 
![image](https://user-images.githubusercontent.com/16046786/119989357-fd579900-bfbe-11eb-9b7e-24c14fd96bfb.png)
6) It works similarly for inputs - only connected inputs will be labelled, and if they come from labelled nodes the node label will be added - otherwise just the socket name will be used. ![image](https://user-images.githubusercontent.com/16046786/119989839-8c64b100-bfbf-11eb-9b07-dbbdbedd8b7b.png)![image](https://user-images.githubusercontent.com/16046786/119989870-9686af80-bfbf-11eb-830e-77ff3fffc759.png)
7) We found it useful - hopefully you do as well :-)


