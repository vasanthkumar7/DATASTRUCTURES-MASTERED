a=[11, 15, 6, 8, 9, 10]
sums=34

def find_sum_exist(a,sums):
    flag=0

    a.sort()

    for i in range(len(a)-1):
        right=i+1
        while right<len(a):
            if a[i]+a[right]==sums:
                return True
            elif a[i]+a[right]<sums:
                right+=1
            else:
                break
    return False

if find_sum_exist(a,sums):
    print("sum exist")
else:
    print("sum do not exist")
        
