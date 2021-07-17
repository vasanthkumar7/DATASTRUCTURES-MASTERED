def sort_based_on_absolutediff(a,k):

    l=[[abs(k-a[i]),a[i]] for i in range(len(a))]
    l.sort()
    for i in range(len(a)):
        a[i]=l[i][1]

    print(a)
    


a=[1,2,3,10,6,5]
sort_based_on_absolutediff(a,7)

