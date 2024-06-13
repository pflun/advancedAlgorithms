# -*- coding: utf-8 -*-
class Solution(object):
    # prefix sum
    def isArraySpecial2(self, nums, queries):
        preSum = [0 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            preSum[i] = preSum[i - 1]
            if nums[i] % 2 != nums[i - 1] % 2:
                # preSum[i] count 连续的valid pairs从0到i
                preSum[i] += 1

        res = []
        for q in queries:
            # 算出两个index之间valid pairs数量
            validPairs = preSum[q[1]] - preSum[q[0]]
            # 如果两个index之间全部都是valid pairs
            if validPairs == q[1] - q[0]:
                res.append(True)
            else:
                res.append(False)
        return res

    # TLE
    def isArraySpecial(self, nums, queries):
        if len(nums) == 1:
            return [True for _ in range(len(queries))]
        validIdx = [[0]]
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                validIdx[-1].append(i - 1)
                validIdx.append([i])
        validIdx[-1].append(len(nums))
        res = []
        for q in queries:
            tmp = False
            for v in validIdx:
                # if found query indexes are within valid special range
                if v[0] <= q[0] and v[1] >= q[1]:
                    tmp = True
            res.append(tmp)
        return res

test = Solution()
print test.isArraySpecial2([1], [[0, 0], [0, 0]])
print test.isArraySpecial2([3,4,1,2,6], [[0,4]])
print test.isArraySpecial2([4,3,1,6], [[0,2],[2,3]])