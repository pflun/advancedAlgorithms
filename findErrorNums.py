class Solution(object):
    def findErrorNums(self, nums):
        if len(nums) == 0:
            return []

        res = []
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key, val in dic.items():
            if val == 2:
                res.append(key)

        for i in range(1, len(nums) + 1):
            if i not in dic:
                res.append(i)

        return res

test = Solution()
print test.findErrorNums([1,2,2,4])