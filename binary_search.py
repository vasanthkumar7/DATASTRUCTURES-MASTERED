def binary_search(a,n):
    left=0
    right=len(a)-1
    

    while left<right:
        mid=int((left+right)/2)
        if a[mid]==n:
            return mid
        else:
            if a[mid]>n:
                right=mid
            else:
                left=mid


    return -1


a=[3,4,5,3,6,37,8]

print("found at "+str(binary_search(a,37)))
            
