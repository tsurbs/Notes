from math import *
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import cm


seed = 10000
np.random.seed(seed)

vector = np.dtype([('x', np.float32), ('y', np.float32)])
gradVectors = np.ndarray(shape=(11, 11), dtype=vector)

for i in gradVectors: 
    for j in i:
        theta = np.random.uniform(0, 2*pi)
        j['x'] = cos(theta)
        j['y'] = sin(theta)

x = gradVectors[:,:]["x"]
y = gradVectors[:,:]["y"]

def perlin(x, y, detail):
    x_i = int(floor(x/detail))
    x_f = int(ceil(x/detail))
    y_i = int(floor(y/detail))
    y_f = int(ceil(y/detail))

    thetaII = sin(x_i*cos(y_i))+1*np.pi
    thetaIF = sin(x_i*cos(y_f))+1*np.pi
    thetaFI = sin(x_f*cos(y_i))+1*np.pi
    thetaFF = sin(x_f*cos(y_f))+1*np.pi

    
    return

mat = np.zeros(shape = (1000, 1000))
mat[:,:]+=.5
# Creates PIL image
im = Image.fromarray(np.uint8(mat * 255) , 'L')

plt.quiver([0,1,2,3,4,5,6,7,8,9,10], [0,1,2,3,4,5,6,7,8,9,10], gradVectors[:,:]["x"], gradVectors[:,:]["y"], color="red")
plt.imshow(im, extent=[0, 10, 0, 10])
plt.show()
print(gradVectors)