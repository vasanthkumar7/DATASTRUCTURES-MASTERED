def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)

def fib_d(n):
    l=[0,1]

    for i in range(2,n+1):
        l.append(l[i-1]+l[i-2])

    return l[n]

print(fib_d(6))
