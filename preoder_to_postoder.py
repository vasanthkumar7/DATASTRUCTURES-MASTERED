
def search_largest_smallest(arr,count):
    small=-1
    largest=-1
    a=arr
    for i in range(count+1,len(arr)):
        if a[count]<a[i]:
            largest=i
            break

    for i in range(count+1,len(arr)):
        if a[count]>a[i]:
            small=i
            break

    return small,largest
def preorder_to_postorder(l,count):
    small,largest=search_largest_smallest(l,count)
    if small!=-1:
        preorder_to_postorder(l,small)

    print(l[count],end=" ")
    if largest!=-1:
        preorder_to_postorder(l,largest)

    

l=[40, 30, 35, 80, 100]

preorder_to_postorder(l,0)    
    
    
