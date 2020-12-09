# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/discuss/952773/PythonJava-simple-O(max(n-k))-method
class Solution(object):
    def minMoves(self, nums, limit):
        delta = collections.Counter()
        n = len(nums)
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            delta[2] += 2
            delta[min(a, b) + 1] -= 1
            delta[a + b] -= 1
            delta[a + b + 1] += 1
            delta[max(a, b) + limit + 1] += 1

        curr = 0
        res = math.inf
        for i in range(2, 2 * limit + 1):
            curr += delta[i]
            res = min(res, curr)
        return res

test = Solution()
print test.minMoves([1,2,4,3], 4)
print test.minMoves([1,2,2,1], 2)
print test.minMoves([1,2,1,2], 2)