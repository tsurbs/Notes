import numpy as np

a = np.array(np.zeros(100000, dtype=int))
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
c = np.array([])
for p in b:
    if p>10000:
        for q in b:
            if q>10000:
                k = p-q
                if float(str(k/(k//(10**(len(str(k))-1)))).replace("1", "0")) == 0:


print(primecount)