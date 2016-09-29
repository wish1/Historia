__author__ = 'student'
input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = input.readline().split()
b=[]
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(a)//2):
        b.append(a[i])
        b.append(a[-i-1])
if len(a)%2==1:
        b.append(a[len(a)//2])
print(' '.join(map(str, a)))
