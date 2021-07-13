a=[1,2,3,4,5,6,7]

print(a[::-1])

for i in range(int(len(a)/2)):
    temp=a[i]
    a[i]=a[len(a)-1-i]
    a[len(a)-1-i]=temp

print(a)
