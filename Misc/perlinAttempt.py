from math import *
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import cm


vector = np.dtype([('x', np.float32), ('y', np.float32)])
gradVectors = np.ndarray(shape=(11, 11), dtype=vector)

for i in gradVectors: 
    for j in i:
        theta = np.random.uniform(0, 2*pi)
        j['x'] = cos(theta)
        j['y'] = sin(theta)

x = gradVectors[:,:]["x"]
y = gradVectors[:,:]["y"]

"""prelimPoints = np.zeros(shape=(1000, 1000))
print(prelimPoints)
for i in range(len(prelimPoints)):
    for j in range(len(prelimPoints[i])): 
        prelimPoints[i,j] = gradVectors[ceil(i/100), ceil(j/100)]['x']*(ceil(i/100)-i/100) + gradVectors[ceil(i/100), ceil(j/100)]['y']*(ceil(j/100)-j/100)
        prelimPoints[i,j] += gradVectors[ceil(i/100), floor(j/100)]['x']*(ceil(i/100)-i/100) + gradVectors[ceil(i/100), ceil(j/100)]['y']*(floor(j/100)-j/100)
        prelimPoints[i,j] += gradVectors[floor(i/100), ceil(j/100)]['x']*(floor(i/100)-i/100) + gradVectors[floor(i/100), ceil(j/100)]['y']*(ceil(j/100)-j/100)
        prelimPoints[i,j] += gradVectors[floor(i/100), floor(j/100)]['x']*(floor(i/100)-i/100) + gradVectors[floor(i/100), floor(j/100)]['y']*(floor(j/100)-j/100)
        prelimPoints[i,j] /= 4
        prelimPoints[i,j] = np.dot([gradVectors[ceil(i/100), ceil(j/100)]['x'], gradVectors[ceil(i/100), ceil(j/100)]['y']], (ceil(i/100)-i/100, ceil(j/100)-j/100))
# gradient between 0 and 1 for 256*256

print(min(prelimPoints[1]))

array = np.linspace(-1,1,256*256)

# reshape to 2d
mat = np.reshape(prelimPoints,(1000,1000))
"""
mat = np.zeros(shape = (1000, 1000))
mat[:,:]+=.5
print(mat)
# Creates PIL image
im = Image.fromarray(np.uint8(mat * 255) , 'L')

plt.quiver([0,1,2,3,4,5,6,7,8,9,10], [0,1,2,3,4,5,6,7,8,9,10], gradVectors[:,:]["x"], gradVectors[:,:]["y"], color="red")
plt.imshow(im, extent=[0, 10, 0, 10])
plt.show()
print(gradVectors)