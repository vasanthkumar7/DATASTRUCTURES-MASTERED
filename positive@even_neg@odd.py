a=[-1, 3, -5, 6, 3, 6, -7, -4, -9, 10]

i=0
positive=[]

negative=[]


for i in range(len(a)-1):
    if i%2==0:
        if a[i]<0 and a[i+1]>0:
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
    else:
        if a[i]>0 and a[i+1]<0:
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp




print(a)
    
