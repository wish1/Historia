__author__ = 'student'
a=[1,2,2,4,5]
k=0
for i in range(len(a)):
    if a.count(a[i])>k:
        k=a.count(a[i])
        j=a[i]
print(j)