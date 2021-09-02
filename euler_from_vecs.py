"""
This script will convert direction into euler angles for area source in PreonLab
Copy and paste standard output result into source placement script.
Run this script using Python3 (not in PreonLab GUI, which does not support Numpy yet
Have fun !
"""

import numpy as np
import math

#INPUT DATA TO CONVERT
index = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16]
dirx = [-0.3482 , 0.96148 , -0.54464 , 0.5807 , 0.09758 , 0 , 0 , 0 , 0.84383 , -0.06853 , -0.19423 , 1 , 1 , -0.37461 , -0.12187 , 0.58779 , 0.52916]
diry = [-0.14608 , -0.25778 , 0.41934 , 0.80175 , 0.96132 , -0.58779 , 0.18738 , -0.08716 , -0.2611 , -0.68073 , -0.91968 , 0 , 0 , 0.9131 , -0.54058 , -0.44062 , -0.80528]
dirz = [0.92597 , 0.09545 , -0.72631 , 0.14137 , 0.25758 , 0.80902 , -0.98229 , -0.99619 , -0.46881 , 0.72932 , 0.34127 , 0 , 0 , -0.161 , 0.83242 , 0.6785 , -0.26742]

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

#CODE
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
