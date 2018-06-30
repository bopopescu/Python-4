import numpy as np
import time

A = np.array([10,20,30,40,50])
B = [10,20,30,40,50]

print(A)
print(B)

p= list(range(10000))
print(p)

q=np.arange(10000)
print(q)

startTime = time.time()
print(startTime)

for elm in p:
    print(elm)

    endTime= time.time()
    print(endTime)

    timeDiff = endTime-startTime
    print(timeDiff)
