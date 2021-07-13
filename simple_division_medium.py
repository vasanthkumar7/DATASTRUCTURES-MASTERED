class Solution:
    def fractionToDecimal(self, numerator, denominator):
        # Code here
        a=numerator/denominator
        f=str(a).split(".")
        g=f[1][0]
        count=1
        while g*(int(len(f[1])/len(g)))!=f[1] and count < len(f[1]):
            g+=f[1][count]
            count+=1
        if count!=len(f[1]):
            d=f[0]+".("+g+")"
        else:
            d=f[0]+"."+g
        
        
        return d


d=Solution()

print(d.fractionToDecimal(16,13 ))
