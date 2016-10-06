__author__ = 'student'
import random
import matplotlib.pyplot as plt
import math
def funct(a=-3,b=3):
    """ищет интеграл функции f(x)"""
    random.seed(0)
    N=1000
    f=0
    for i in range(N):
        x=random.uniform(a,b)
        f+=math.sin(x**2+3)
    p=f*(b-a)/N
    return(p)
print(funct(0,5))




