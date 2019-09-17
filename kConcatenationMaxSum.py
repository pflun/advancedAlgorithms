class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        neg = False
        allNeg = False
        for a in arr:
            if a < 0:
                neg = True
            else:
                allNeg = True
        if not allNeg:
            return 0
        if neg == False:
            sumVal = sum(arr) * k
            return sumVal % (10 ** 9 + 7)
        else:
            maxSame = 0
            tmp = 0
            for a in arr:
                if a < 0:
                    maxSame = max(maxSame, tmp)
                    tmp = 0
                else:
                    tmp += a
                maxSame = max(maxSame, tmp)
            maxDiff = 0
            tmp = 0
            doubleArr = arr + arr
            print doubleArr
            for a in doubleArr:
                if a < 0:
                    maxDiff = max(maxDiff, tmp)
                    tmp = 0
                else:
                    tmp += a
                maxDiff = max(maxDiff, tmp)
            if maxSame >= maxDiff:
                return maxSame % (10 ** 9 + 7)
            else:
                return maxDiff % (10 ** 9 + 7)

test = Solution()
print test.kConcatenationMaxSum([-5,-2,0,0,3,9,-2,-5,4], 5)