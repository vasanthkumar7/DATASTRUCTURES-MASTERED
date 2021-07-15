# Python 3 program to demonstrate working of Square Root
# Decomposition.
from math import sqrt

MAXN = 10000
SQRSIZE = 100

arr = [0]*(MAXN)		 # original array
block = [0]*(SQRSIZE)	 # decomposed array
blk_sz = 0				 # block size

# Time Complexity : O(1)
def update(idx, val):
	blockNumber = idx // blk_sz
	block[blockNumber] += val - arr[idx]
	arr[idx] = val

# Time Complexity : O(sqrt(n))
def query(l, r):
	sum = 0
	while (l < r and l % blk_sz != 0 and l != 0):
		
		# traversing first block in range
		sum += arr[l]
		l += 1
	
	while (l + blk_sz <= r):
		
		# traversing completely overlapped blocks in range
		sum += block[l//blk_sz]
		l += blk_sz
	
	while (l <= r):
		
		# traversing last block in range
		sum += arr[l]
		l += 1
	
	return sum
	
# Fills values in input[]
def preprocess(input, n):
	
	# initiating block pointer
	blk_idx = -1

	# calculating size of block
	global blk_sz
	blk_sz = int(sqrt(n))

	# building the decomposed array
	for i in range(n):
		arr[i] = input[i];
		if (i % blk_sz == 0):
			
			# entering next block
			# incrementing block pointer
			blk_idx += 1;
		
		block[blk_idx] += arr[i]

# Driver code

# We have used separate array for input because
# the purpose of this code is to explain SQRT
# decomposition in competitive programming where
# we have multiple inputs.
input= [1, 5, 2, 4, 6, 1, 3, 5, 7, 10]
n = len(input)

preprocess(input, n)

print("query(3,8) : ",query(3, 8))
print("query(1,6) : ",query(1, 6))
update(8, 0)
print("query(8,8) : ",query(8, 8))

# This code is contributed by Sanjit_Prasad
