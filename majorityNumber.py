class Solution:
    def majorityNumber(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        for key, val in dic.items():
            if val > len(nums)/2:
                return key

test = Solution()
print test.majorityNumber([2,2,2,1,3,3,5,6])