# https://www.youtube.com/watch?v=HWJEMKWzy-Q
class Solution(object):
    def numTrees(self, n):
        if n < 1:
            return 0
        # nums[i] store how many structurally unique BST at i
        nums = [0] * (n + 1)
        # init
        nums[0] = 1
        nums[1] = 1

        for i in range(2, n + 1):
            for j in range(i):
                # left: j; right i - left - root(1), for each i, nums[i] is for (0 ~ i) left child ways * right child ways
                nums[i] += (nums[j] * nums[i - j - 1])

        return nums[n]

test = Solution()
print test.numTrees(3)