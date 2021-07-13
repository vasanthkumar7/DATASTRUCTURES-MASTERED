a=[-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]

for i in range(len(a)):
    print(i)
    if i in a:
        temp=a[a.index(i)]
        a[a.index(i)]=a[i]
        a[i]=temp

print(a)
