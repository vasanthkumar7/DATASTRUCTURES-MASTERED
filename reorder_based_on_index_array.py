arr=[50,40,70,60,90]

index=[3,0,4,1,2]

for i in range(len(index)):
    temp=arr[index[i]]
    arr[index[i]]=arr[i]
    arr[i]=temp

    temp=index[index[i]]
    index[index[i]]=index[i]
    index[i]=temp

print(arr)
print(index)

