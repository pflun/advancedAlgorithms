class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def findPosition(self, A, target):
        for i in range(len(A)):
            if A[i] == target:
                return i
        return False

    # Binary search
    def findPosition2(self, A, target):
        low = 0
        high = len(A) - 1
        while A[low] != A[high]:
            mid = (high + low) / 2
            if A[mid] > target:
                high = mid
            elif A[mid] < target:
                low = mid
            if A[mid] == target:
                return mid
        return False


test = Solution()
print test.findPosition2([1,2,2,4,5,5], 6)