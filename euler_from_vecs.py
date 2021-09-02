"""
This script will convert direction into euler angles for area source in PreonLab
Copy and paste standard output result into source placement script.
Run this script using Python3 (not in PreonLab GUI, which does not support Numpy yet
Have fun !
"""

import numpy as np
import math

#INPUT DATA TO CONVERT
index = [0 , 1 , 2]
dirx = [0, 0, 0]
diry = [0, 0, 0]
dirz = [0, 0, 0]

#CODE
def euler_from_vecs(a=None, b=None):
	"""
	Filename: align_vecotrs.py
	Created Date: Friday, May 20th 2020, 6:12:09 pm
	Author: Shreyas Joshi - Fifty2 Technology GmbH
	Email: shreyas.joshi@fifty2.eu
	
	Calculates euler angles to make vector a point in the direction of vector b
	Parameters
	----------
	a : (x,y,z) vector (optional)
		default value (0,-1,0) pointing direction of AreaSource in PL-v4.2
		when its euler angles are (0,0,0)
	b : (x,y,z) vector
	Returns
	-------
	(PHI,THETA, PSI) for inputting in PreonLab
	"""
	a, b = a / np.linalg.norm(a), b / np.linalg.norm(b)
	v = np.cross(a, b)
	c = np.dot(a, b)
	s = np.linalg.norm(v)
	I = np.identity(3)
	K = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
	R = I + K + K @ K * ((1 - c) / (s ** 2))
	sy = math.sqrt(R[0, 0] * R[0, 0] + R[1, 0] * R[1, 0])
	singular = sy < 1e-6
	if not singular:
		x = math.atan2(R[2, 1], R[2, 2])
		y = math.atan2(-R[2, 0], sy)
		z = math.atan2(R[1, 0], R[0, 0])
	else:
		x = math.atan2(-R[1, 2], R[1, 1])
		y = math.atan2(-R[2, 0], sy)
		z = 0
	return np.array([x, y, z]) * 180 / np.pi

euler_angle_x = []
euler_angle_y = []
euler_angle_z = []

for i in index :
	input = np.array([dirx[i], diry[i], dirz[i]])
	res = euler_from_vecs(a = [0,-1,0], b = input)
	euler_angle_x.append(res[0])
	euler_angle_y.append(res[1])
	euler_angle_z.append(res[2])

print ("euler_angle_x = ", euler_angle_x)
print ("euler_angle_y = ", euler_angle_y)
print ("euler_angle_z = ", euler_angle_z)
