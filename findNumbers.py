class Solution(object):
    def findNumbers(self, nums):
        res = 0
        for n in nums:
            strN = str(n)
            if len(strN) % 2 == 0:
                res += 1
        return res

test = Solution()
print test.findNumbers([12,345,2,6,7896])
print test.findNumbers([555,901,482,1771])
print test.findNumbers([])