from math import *
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import cm
from scipy import interpolate

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
    x_i = int(floor(x/detail))*detail
    x_f = int(ceil(x/detail))*detail
    y_i = int(floor(y/detail))*detail
    y_f = int(ceil(y/detail))*detail

    if x_i == x and y_i == y: return 1;

    np.random.seed(x_i^y_i)
    thetaII = np.random.uniform(0,2*np.pi)
    np.random.seed(x_i^y_f)
    thetaIF = np.random.uniform(0,2*np.pi)
    np.random.seed(x_f^y_i)
    thetaFI = np.random.uniform(0,2*np.pi)
    np.random.seed(x_f^y_f)
    thetaFF = np.random.uniform(0,2*np.pi)

    #print(x_i, x_f, y_i, y_f)
    #print(thetaII, thetaIF, thetaFI, thetaFF)

    displII = [(x-x_i),(y-y_i)]
    displIF = [(x-x_i),(y-y_f)]
    displFI = [(x-x_f),(y-y_i)]
    displFF = [(x-x_f),(y-y_f)]

    dotII = np.dot([sin(thetaII), cos(thetaII)],displII)
    dotIF = np.dot([sin(thetaIF), cos(thetaIF)],displIF)
    dotFI = np.dot([sin(thetaFI), cos(thetaFI)],displFI)
    dotFF = np.dot([sin(thetaFF), cos(thetaFF)],displFF)

    f = interpolate.interp2d([x_i,x_f],[y_i,y_f],[[dotII,dotIF], [dotFI, dotFF]], kind="linear")
    return f(x,y)/detail

x=[]
for i in range(100):
    for j in range(100):
        x.append(perlin(i,j,10))+1*127

print(max(x))

# Creates PIL image
im = Image.fromarray(np.uint8(x , 'L'))
plt.imshow(im, extent=[0, 10, 0, 10])
plt.show()
