a=[7, 10, 4, 3, 20, 15]

k=3

count=0

def find_kth_largest_number(a,k):
    count=0
    while count<k-1:
        a.remove(max(a))
        count+=1
        
    return max(a)

print(find_kth_largest_number(a,k))

