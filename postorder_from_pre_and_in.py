# Python3 program to print postorder
# traversal from preorder and inorder
# traversals

# A utility function to search x in
# arr[] of size n
def search(arr, x, n):
	
	for i in range(n):
		if (arr[i] == x):
			return i

	return -1

# Prints postorder traversal from
# given inorder and preorder traversals
def printPostOrder(In, pre, n):
	
	# The first element in pre[] is always
	# root, search it in in[] to find left
	# and right subtrees
	root = search(In, pre[0], n)

	# If left subtree is not empty,
	# print left subtree
	if (root != 0):
		printPostOrder(In, pre[1:n], root)

	# If right subtree is not empty,
	# print right subtree
	if (root != n - 1):
		printPostOrder(In[root + 1 : n],
					pre[root + 1 : n],
					n - root - 1)

	# Print root
	print(pre[0], end = " ")

# Driver code
In = [ 4, 2, 5, 1, 3, 6 ]
pre = [ 1, 2, 4, 5, 3, 6 ]
n = len(In)

print("Postorder traversal ")

printPostOrder(In, pre, n)

# This code is contributed by avanitrachhadiya2155
