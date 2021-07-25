a=[1,101,2,3,100,4,5]


l=a[0:]

for i in range(1,len(a)):
    for j in range(i):
        if a[i]>a[j] and l[i]<l[i]+a[j]:
            l[i]=l[i]+a[j]

print(max(l),l,a)
