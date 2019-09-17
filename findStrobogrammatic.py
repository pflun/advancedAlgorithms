class Solution(object):
    # missed edge case: n = 4:   1001, 6009, 8008, 9006...
    def findStrobogrammatic(self, n):
        res = [[''], ['0', '1', '8']]
        if n == 0:
            return res[0]
        elif n == 1:
            return res[1]
        for i in range(2, n + 1):
            tmp = []
            for r in res[i - 2]:
                tmp.append('1' + r + '1')
                tmp.append('6' + r + '9')
                tmp.append('8' + r + '8')
                tmp.append('9' + r + '6')
            res.append(tmp)
        return res[-1]

test = Solution()
print test.findStrobogrammatic(4)
