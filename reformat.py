class Solution(object):
    def reformat(self, s):
        nums = []
        chars = []
        for c in s:
            if c.isdigit():
                nums.append(c)
            else:
                chars.append(c)
        if abs(len(nums) - len(chars)) >= 2:
            return ''
        res = ''
        if len(nums) > len(chars):
            for i in range(len(chars)):
                res += nums[i]
                res += chars[i]
            res += nums[-1]
        else:
            for i in range(len(nums)):
                res += chars[i]
                res += nums[i]
            if len(nums) == len(chars):
                return res
            else:
                res += chars[-1]
        return res

test = Solution()
print test.reformat("a0b1c2")
print test.reformat("leetcode")
print test.reformat("1229857369")
print test.reformat("covid2019")
print test.reformat("ab123")