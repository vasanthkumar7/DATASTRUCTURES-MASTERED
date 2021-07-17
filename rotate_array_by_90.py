a=[ [1, 2, 3, 4 ],
        [5, 6, 7, 8 ],
        [9, 10, 11, 12 ],
        [13, 14, 15, 16 ] ]
mat=a
N=len(a)
for x in range(int(len(a)/2)):
    for y in range(x,len(a)-1-x):
        temp = mat[x][y]
 
            # move values from right to top
        mat[x][y] = mat[y][N-1-x]
 
            # move values from bottom to right
        mat[y][N-1-x] = mat[N-1-x][N-1-y]
 
            # move values from left to bottom
        mat[N-1-x][N-1-y] = mat[N-1-y][x]
 
            # assign temp to left
        mat[N-1-y][x] = temp


for i in a:
    print(i)
       
