def missingnum(array,n):
    if n not in array:
        return n
    array.sort()
    count=1
    for i in array:
        if count!=i:
            return count
        count+=1

print(missingnum([3,4,5,1],5))
        
