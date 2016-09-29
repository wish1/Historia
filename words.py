__author__ = 'student'
a=[1,2,3,4,5]
for i in range(1,len(a),2):
    a[i-1],a[i]=a[i],a[i-1]
print(' '.join(map(str, a)))
