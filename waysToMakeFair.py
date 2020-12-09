class Solution(object):
    def waysToMakeFair(self, nums):
        res = 0
        preSumOdd = []
        preSumEven = [0, nums[0]]
        for i in range(1, len(nums)):
            if i % 2 != 0:
                if not preSumOdd:
                    preSumOdd.append(nums[i])
                    preSumEven.append(preSumEven[-1])
                else:
                    preSumOdd.append(preSumOdd[-2] + nums[i])
                    preSumEven.append(preSumEven[-1])
            else:
                if not preSumEven:
                    preSumEven.append(nums[i])
                    preSumOdd.append(preSumOdd[-1])
                else:
                    preSumEven.append(preSumEven[-2] + nums[i])
                    preSumOdd.append(preSumOdd[-1])
        preSumOdd = [0] + preSumOdd
        for i in range(len(nums)):
            even = preSumEven[i] + preSumOdd[-1] - preSumOdd[i]
            odd = preSumOdd[max(i - 1, 0)] + preSumEven[-1] - preSumEven[i + 1]
            if even == odd:
                res += 1
        return res

test = Solution()
print test.waysToMakeFair([2,1,6,4])
print test.waysToMakeFair([1,1,1])
print test.waysToMakeFair([1,2,3])