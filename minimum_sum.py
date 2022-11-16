import itertools




def findMinRec(arr, i, sumCalculated,
			sumTotal):

	# If we have reached last element.
	# Sum of one subset is sumCalculated,
	# sum of other subset is sumTotal-
	# sumCalculated. Return absolute
	# difference of two sums.
	if (i == 0):
		return abs((sumTotal - sumCalculated) -
				sumCalculated)

	# For every item arr[i], we have two choices
	# (1) We do not include it first set
	# (2) We include it in first set
	# We return minimum of two choices
	return min(findMinRec(arr, i - 1,
						sumCalculated+arr[i - 1],
						sumTotal),
			findMinRec(arr, i - 1,
						sumCalculated, sumTotal))

# Returns minimum possible
# difference between sums
# of two subsets


def findMin(arr, n):

	# Compute total sum
	# of elements
	sumTotal = sum(arr[i] for i in range(n))
	# Compute result using
	# recursive function
	return findMinRec(arr, n,
					0, sumTotal)


# Driver code
if __name__ == "__main__":

	arr = [3, 1, 4, 2, 2, 1]
	n = len(arr)
	print("The minimum difference " +
		"between two sets is ",
		findMin(arr, n))

# This code is contributed by Chitranayal



# A Recursive Python3 program to solve
# minimum sum partition problem.
import sys

# Returns the minimum value of the
# difference of the two sets.


def findMin(a, n):

	su = 0

	# Calculate sum of all elements
	su = sum(a)

	# Create an 2d list to store
	# results of subproblems
	dp = [[0 for _ in range(su + 1)] for _ in range(n + 1)]

	# Initialize first column as true.
	# 0 sum is possible
	# with all elements.
	for i in range(n + 1):
		dp[i][0] = True

	# Initialize top row, except dp[0][0],
	# as false. With 0 elements, no other
	# sum except 0 is possible
	for j in range(1, su + 1):
		dp[0][j] = False

	# Fill the partition table in
	# bottom up manner
	for i, j in itertools.product(range(1, n + 1), range(1, su + 1)):
		# If i'th element is excluded
		dp[i][j] = dp[i - 1][j]

		# If i'th element is included
		if a[i - 1] <= j:
			dp[i][j] |= dp[i - 1][j - a[i - 1]]

	return next((su - (2 * j) for j in range(su // 2, -1, -1) if dp[n][j] == True), sys.maxsize)


# Driver code
a = [3, 1, 4, 2, 2, 1]
n = len(a)

print("The minimum difference between "
	"2 sets is ", findMin(a, n))

# This code is contributed by Tokir Manva


print(minimum_difference([3,-2,1,5,-3,-12]))