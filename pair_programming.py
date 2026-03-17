import numpy as np
#Function that takes r and theta as input and outputs the x and y cooridnates 
def polar_to_cartesian(r, theta):
    x= r * np.cos(theta)
    y = r* np.sin(theta)
    return x,y

#Feedback: 
#The function is correct and easy to read.
#Adding a comment explaining the inputs would make it even clearer.