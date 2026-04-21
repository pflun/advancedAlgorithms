class Solution:
    def addSignedArrays(self, num1, num2):
        return self.parseArray(num1) + self.parseArray(num2)

    def parseArray(self, num):
        isNegative = False
        endIdx = -1
        if num[0] == '-':
            isNegative = True
            endIdx = 0
        tens = 1
        res = 0
        for i in range(len(num) - 1, endIdx, -1):
            res += int(num[i]) * tens
            tens *= 10
        if isNegative:
            return -res
        else:
            return res

test = Solution()
print test.addSignedArrays(["1","2"], ["5"])
print test.addSignedArrays(["-","1","0"], ["4"])
print test.addSignedArrays(["0"], ["0"])