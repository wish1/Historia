__author__ = 'student'
import math
def funct(x):
    f=math.sin(x**2+3)
    return(f)
def integr(a,b):
    N=1000
    d=0
    for i in range(N):
        d+=funct(a+(i+1/2)*(b-a)/N)*((b-a)/N)
    return(d)
print(integr(0,5))