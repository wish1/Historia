__author__ = 'student'
n=int(input())
b=[]
a=1
for i in range(n):
    for j in range(1,i):
        a*=((i-j)/j)
    b[i]=a
    print(' '.join(map(str, a)))

