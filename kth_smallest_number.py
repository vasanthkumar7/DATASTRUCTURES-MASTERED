def kth_smallest_number(a,k):
    count=0
    while count<k-1:
        a.remove(min(a))
        count+=1

    return min(a)


a=[4,6,36,7,4,8,4,8,3]
k=3

print(kth_smallest_number(a,k))

