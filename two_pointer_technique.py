def sums(a,s):
    a.sort()

    i=0
    j=len(a)-1

    while i<j:
        if a[i]+a[j]==s:
            return True
        elif a[i]+a[j]>s:
            j-=1
        else:
            i+=1
    return False

a=[1,3,52,2,6,7,2,9]
s=454

if sums(a,s):
    print("present")
else:
    print("not present")
