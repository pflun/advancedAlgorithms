# Given a permutation of numbers from 1 to n in any order.
# Determine the minimum number of operations required to make the sequence strictly increasing.
# In one operation, you can move any element to the front or end of the sequence.
# Example:
# Input: 4 1 2 5 3
# Output: 2
# Explanation:
# First operation: move 4 to the end
# Second operation: move 5 to the end
class Solution(object):
    def minOperationsToIncreasingSequence(self, arr):
        n = len(arr)

        # Initialize the dp array, where dp[i] will store the length of the longest increasing
        # subsequence that ends with arr[i].
        dp = [1] * n

        # Find the LIS using DP.
        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The length of the LIS is the maximum value in dp.
        length_of_LIS = max(dp)

        # Minimum operations needed is the number of elements not in the LIS.
        min_operations = n - length_of_LIS

        return min_operations

test = Solution()
print test.minOperationsToIncreasingSequence([4, 1, 2, 5, 3])
# Output should be 2
