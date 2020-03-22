class Solution(object):
    def numTimesAllBlue(self, light):
        res = 0
        currMax = 0
        count = 0
        for l in light:
            currMax = max(currMax, l)
            count += 1
            if count == currMax:
                res += 1
        return res

test = Solution()
print test.numTimesAllBlue([2,1,3,5,4])
print test.numTimesAllBlue([3,2,4,1,5])
print test.numTimesAllBlue([4,1,2,3])
print test.numTimesAllBlue([2,1,4,3,6,5])
print test.numTimesAllBlue([1,2,3,4,5,6])