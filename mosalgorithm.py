array=[1, 1, 2, 1, 3, 4, 5, 2, 8]
querry=[[0, 4], [1, 3], [2, 4]]


def mosalgorithm(array,querry):
    for i in querry:
        currL,currR,currsum=0,0,0

        L,R=i

        while currL<L:
            currsum-=array[currL]
            currL+=1
        while currL>L:
            currsum+=array[currL-1]
            currL-=1
        while currR<=R:
            currsum+=array[currR]
            currR+=1

        while currR>R+1:
            currsum-=array[currR-1]
            currR-=1

        print(currsum)

mosalgorithm(array,querry)

        
            
