class Solution(object):
    # buggy
    def sequentialDigits(self, low, high):
        if low == high:
            return []
        curr = self.getNext(low)
        res = [curr]
        while self.getNext(curr) <= high:
            curr = self.getNext(curr)
            res.append(curr)
        return res

    def getNext(self, curr):
        res = ""
        if not self.isValid(curr) :
            tmp = 1
            for _ in range(len(str(curr))):
                res += str(tmp)
                tmp += 1
        elif curr % 10 == 9:
            tmp = 1
            for _ in range(len(str(curr)) + 1):
                res += str(tmp)
                tmp += 1
        else:
            strCurr = str(curr)
            for c in strCurr:
                nc = int(c) + 1
                res += str(nc)
        return int(res)

    def isValid(self, curr):
        strCurr = str(curr)
        for i in range(len(strCurr) - 1):
            if strCurr[i + 1] <= strCurr[i]:
                return False
        return True

test = Solution()
print test.sequentialDigits(100, 300)
print test.sequentialDigits(1000, 13000)