__author__ = 'student'
input = open('marks', 'r')
output = open('output.txt', 'w')
a = input.read().split()
for i in range(len(a)):
    a[i]=int(a[i])

n=10
k=0
for i in range(n):
    if a[i]==2:
        k=1
    if a[i]!=2 and k==1:
        a[i-1]=0
        n-=1
        k=0
    print(a[i])
s=int((sum(a))/n)
print(s)