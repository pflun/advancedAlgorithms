class Solution(object):
    def binaryGap(self, N):
        bi = bin(N)
        res = 0
        for i in range(len(bi)):
            if bi[i] == "1":
                idx = bi[i + 1:].find("1")
                res = max(res, idx + 1)
        return res

test = Solution()
print test.binaryGap(22)