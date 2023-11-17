import time
import math
x=math.pow(10,int(input()))
a=1
b=[]
s=time.time()
while a-1!=x:
    if (x/a) % 1 == 0:
        b.append(x/a)
    a+=1
t=time.time()-s
print(str(t*1000)+" ms")
print(b)