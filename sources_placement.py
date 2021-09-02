"""
This script will place and set your sources from a list
Copy and paste it in PreonLab Python GUI
You may need to convert your sources direction (normal vector to source) into euler angles using euler_from_vecs.py
Have fun !
"""

import preonpy
import math

s = preonpy.current_scene

#INPUT DATA
#Name = [M21 , M12 , M23]
index = [0 , 1 , 2]
diameter = [0, 0, 0]
dirx = [0, 0, 0]
diry = [0, 0, 0]
dirz = [0, 0, 0]
posx = [0, 0, 0]
posy = [0, 0, 0]
posz = [0, 0, 0]
flow_rate = [0, 0, 0]

#CONVERTED DATA
#Convertion using euler_from_vecs.py :
euler_angle_x =  [0, 0, 0]
euler_angle_y =  [0, 0, 0]
euler_angle_z =  [0, 0, 0]

#CODE
for i in index :
	source = s.create_object("Area source")
	source["area type"] = "Circle"
	source["scale"] = [diameter[i] / 1000, diameter[i] / 1000, diameter[i] / 1000]
	source["position"] = [posx[i], posy[i], posz[i]]
	source["inflow unit"] = "volumeFlowRate"
	source["volume flow rate"] = flow_rate[i]
	source["euler angles"] = [euler_angle_x[i], euler_angle_y[i], euler_angle_z[i]]
	"""
	#Rain mode allows to force right emitting speed, but particle cohesion will be lost
	#Normal mode : Iooooooooo
	#Rain mode : Io  o  o  o  o  o  o  o
	source["emit type"] = "rain"
	source["emit velocity"] = flow_rate[i] / (math.pi * ((diameter[i] / 1000)**2) / 4)
	"""
