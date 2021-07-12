def trailingzeros_factorial(N):
    j = 5
    ans = 0
    while j<=N:
        ans=ans+N//j
        j=j*5
    return ans
    
print(trailingzeros_factorial(10))
