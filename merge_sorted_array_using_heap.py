from heapq import heapify,heappush,heappop

a=[[1,2,3,4],[1,2,3,5,6,7,8],[9,10,11,12]]

heap=[]

heapify(heap)

for i in a:
    for j in i:
        heappush(heap,j)
for i in heap:
    print(i,end=" ")
