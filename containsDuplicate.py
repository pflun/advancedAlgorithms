class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) == 0:
            return False

        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        for key, val in dic.items():
            if val > 1:
                return False
        return True

# Solution 2, use set then check len(), smaller means duplicate exists

test = Solution()
print test.containsDuplicate([-2,3,-4])