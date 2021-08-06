
def search(arr, x, n):
	for i in range(n):
		if (arr[i] == x):
			return i
	return -1


def printPostOrder(In, pre, n):
	
	root = search(In, pre[0], n)

	
	if (root != 0):
		printPostOrder(In, pre[1:n], root)

	
	if (root != n - 1):
		printPostOrder(In[root + 1 : n],
					pre[root + 1 : n],
					n - root - 1)

	print(pre[0], end = " ")

# Driver code
In = [ 4, 2, 5, 1, 3, 6 ]
pre = [ 1, 2, 4, 5, 3, 6 ]
n = len(In)

print("Postorder traversal ")

printPostOrder(In, pre, n)

# This code is contributed by avanitrachhadiya2155
