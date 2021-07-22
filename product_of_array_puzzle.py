a=[10,3,5,6,2]

l=[]

for i in range(len(a)):
    fact=1
    for j in range(len(a)):
        if i!=j:
            fact*=a[j]
    
    l.append(fact)

print(l)
