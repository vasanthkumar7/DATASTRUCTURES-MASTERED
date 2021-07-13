def rotate_array(a,d):
    a[:d]=reversed(a[:d])
    a[d:]=reversed(a[d:])
    a[0:]=reversed(a[0:])

a=[1,2,3,4,5,6]

rotate_array(a,3)
print(a)
