import numpy as np
#Function that takes r and theta as input and outputs the x and y cooridnates 
def polar_to_cartesian(r, theta):
    x= r * np.cos(theta)
    y = r* np.sin(theta)
    return x,y
