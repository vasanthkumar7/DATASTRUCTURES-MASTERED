import random


def shuffle(a):

    for i in range(len(a)-1,0,-1):
        j=random.randint(0,i+1)
        a[i],a[j]=a[j],a[i]

a=[2,4,5,687,14,1,4,6,2,7]

shuffle(a)

print(a)
