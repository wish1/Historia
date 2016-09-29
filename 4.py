__author__ = 'student'
input = open('input3.txt', 'r')
output = open('output.txt', 'w')
a = input.read().split()
for i in range(len(a)):
    a[i]=int(a[i])
t=a.pop()

b=len(a)
for i in range(t):
    a.insert(b-a[b-1]-1,a[b-1])
    a.pop()
print(' '.join(map(str, a)))
