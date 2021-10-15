import matplotlib.pyplot as plt
import numpy as np

state = np.array([[0,0], [0,1], [1,1]])

def numAround(i, j):
    retC = np.where(state == [i,j])
    retB =  retC[0].size != 0
    retA = 0

    retA += np.where(state == [i+1,j])[0].size
    retA += np.where(state == [i,j+1])[0].size
    retA += np.where(state == [i+1,j+1])[0].size
    retA += np.where(state == [i-1,j])[0].size
    retA += np.where(state == [i,j-1])[0].size
    retA += np.where(state == [i-1,j-1])[0].size
    retA += np.where(state == [i-1,j+1])[0].size
    retA += np.where(state == [i+1,j-1])[0].size

    return [retA, retB, retC]

def advance(statep):

    maxX = statep[0][0]
    maxY = statep[0][1]
    minX = statep[0][0]
    minY = statep[0][1]
    for x in statep:
        if x[0] > maxX: maxX = x[0]
        if x[1] > maxY: maxY = x[1]

        if x[0] < minX: minX = x[0]
        if x[1] < minY: minY = x[1]

    for i in range(minX-2, maxX+2):
        for j in range(minY-2, maxX+2):
            NA = numAround(i,j)
            print(i,j,NA)
            if NA[0] >= 3 and not NA[1]:
                np.append(state, [i,j])
                
            elif NA[0] < 2 and NA[1]:
                np.delete(state, NA[2][0][0])
    
    return plt.scatter(np.transpose(state)[0], np.transpose(state)[1])


advance(state)
print(state)