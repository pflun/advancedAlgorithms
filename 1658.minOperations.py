# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/935935/Java-Detailed-Explanation-O(N)-Prefix-SumMap-Longest-Target-Sub-Array
# question can translate to a subarray in the middle of original array whose sum is == totalSum - x
# then translate to Find the Longest Subarray with Sum Equals to TotalSum - X
class Solution(object):
    def minOperations(self, nums, x):
        res = 0
        preSum = [0]
        target = sum(nums) - x
        # corner case: remove all elements to reach to 0
        if target == 0:
            return len(nums)
        dic = {}
        for n in nums:
            preSum.append(n + preSum[-1])
        for i in range(len(preSum)):
            if preSum[i] - target in dic:
                res = max(res, i - dic[preSum[i] - target])
            dic[preSum[i]] = i
        return -1 if res == 0 else len(nums) - res

test = Solution()
print test.minOperations([1,1,4,2,3], 5)
print test.minOperations([5,6,7,8,9], 4)
print test.minOperations([3,2,20,1,1,3], 10)
print test.minOperations([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], 134365)