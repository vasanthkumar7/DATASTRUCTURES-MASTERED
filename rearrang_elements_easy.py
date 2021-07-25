a=[-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]

for i in range(len(a)):
    if i in a:
        temp=a[a.index(i)]
        a[a.index(i)]=a[i]
        a[i]=a[a.index(i)]
    

print(a)
