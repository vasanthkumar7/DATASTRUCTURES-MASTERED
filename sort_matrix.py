a=[ [ 5, 4, 7 ],
        [ 1, 3, 8 ],
        [ 2, 9, 6 ] ]

temp=[0]*(len(a)*len(a))

k=0

for i in range(len(a)):
    for j in range(len(a)):
        temp[k]=a[i][j]
        k+=1

temp.sort()
k=0
for i in range(len(a)):
    for j in range(len(a)):
        a[i][j]=temp[k]
        k+=1

for i in a:
    print(i)
