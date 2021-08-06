"""Python3 program for finding postorder
traversal of BST from preorder traversal"""

INT_MIN = -2**31
INT_MAX = 2**31

# Function to find postorder traversal
# from preorder traversal.


def findPostOrderUtil(pre, n, minval,
					maxval, preIndex):

	# If entire preorder array is traversed
	# then return as no more element is left
	# to be added to post order array.
	if (preIndex[0] == n):
		return

	# If array element does not lie in
	# range specified, then it is not
	# part of current subtree.
	if (pre[preIndex[0]] < minval or
			pre[preIndex[0]] > maxval):
		return

	# Store current value, to be printed later,
	# after printing left and right subtrees.
	# Increment preIndex to find left and right
	# subtrees, and pass this updated value to
	# recursive calls.
	val = pre[preIndex[0]]
	preIndex[0] += 1

	# All elements with value between minval
	# and val lie in left subtree.
	findPostOrderUtil(pre, n, minval,
					val, preIndex)

	# All elements with value between val
	# and maxval lie in right subtree.
	findPostOrderUtil(pre, n, val,
					maxval, preIndex)

	print(val, end=" ")

# Function to find postorder traversal.


def findPostOrder(pre, n):

	# To store index of element to be
	# traversed next in preorder array.
	# This is passed by reference to
	# utility function.
	preIndex = [0]

	findPostOrderUtil(pre, n, INT_MIN,
					INT_MAX, preIndex)


# Driver Code
if __name__ == '__main__':
	pre = [40, 30, 35, 80, 100]

	n = len(pre)

	# Calling function
	findPostOrder(pre, n)

# This code is contributed by
# SHUBHAMSINGH10
