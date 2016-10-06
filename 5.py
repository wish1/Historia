__author__ = 'student'
import numpy as np
values=[3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
file_input = open('input.txt', 'r')
def get_percentile(values, bucket_number):
    a=[0.0]
    for i in range(1,bucket_number):
        a.append(np.percentile(values,i*100/(bucket_number)))
    return(a)

def get_percentile_number(value,percentiles):
    k=[]
    m=0
    for j in range (len(value)):
        for i in range(len(percentiles)-1):
            if percentiles[i]<=value[j] and value[j] < percentiles[i+1]:
                k.append(percentiles[i])
                m=1
        if m!=0:
            m=0
        elif value[j]<percentiles[0]:
            k.append(percentiles[0])
        else: k.append(percentiles[-1])
    return(k)

def values_equalization(values, percentiles):
    b=get_percentile_number(values,percentiles)
    for i in range(len(b)):
        b[i]=b[i]/len(values)
    return(b)

percentiles=get_percentile(values,4)
print(get_percentile(values,4))
print(get_percentile_number(values,percentiles))
print(values_equalization(values, percentiles))
