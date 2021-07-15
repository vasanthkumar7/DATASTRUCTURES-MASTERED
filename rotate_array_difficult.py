a =[
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ] 
        ]
c=[
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ] 
        ]
corners=len(a[0])
top=0

bottom=len(a)-1

left=0
df=a[0:]
right=len(a[0])-1
for i in a:
    print(i)

print("")
while corners>1:
    lists=[]
    for i in range(left,right+1):
        lists.append([top,i])

    for i in range(top+1,bottom ):
        lists.append([i,right])
    for i in range(right,left-1,-1):
        lists.append([bottom,i])
    for i in range(bottom-1,top,-1):
        lists.append([i,top])
    klist=[lists[-1]]+lists[0:len(lists)-1]
    for i in range(len(lists)):
        a[lists[i][0]][lists[i][1]]=c[klist[i][0]][klist[i][1]]

    top+=1
    bottom-=1
    left+=1
    right-=1
    corners-=2

    

    print("")

for i in a:
    print(i)
    
