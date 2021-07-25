def alternatesort(a):
    a.sort()

    i=0
    j=len(a)-1

    while i<j:
        print(a[j],end=" ")
        j-=1
        print(a[i],end=" ")
        i+=1
    if i%2==0:
        print(a[i])

a=[45,26,31,2,1,7,4,8,3]

alternatesort(a)
