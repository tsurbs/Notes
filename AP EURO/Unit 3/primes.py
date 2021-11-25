import numpy as np

a = np.array(np.zeros(1000000, dtype=int))
b = np.array([2])
def isPrime(c):
    for i in b:
        if c%(i) == 0:
            return False
    return True
primecount = 0;
for i in range(2, a.size):
    if a[i] == 0:
        if isPrime(i):
            primecount+=1
            a[i] = primecount
            b = (np.append(b,i))
            if primecount == 10000: print(i)
        else: 
            a[i] = -1

print(primecount)