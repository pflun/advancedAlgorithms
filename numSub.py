class Solution(object):
    def numSub(self, s):
        res = 0
        idx = 0
        length = 0
        while idx < len(s):
            if s[idx] == '1':
                length += 1
                idx += 1
            else:
                for k in range(1, length + 1):
                    res += k
                length = 0
                while idx < len(s):
                    if s[idx] == '1':
                        break
                    idx += 1
        if s[-1] == '1':
            for k in range(1, length + 1):
                res += k
        return res % (10 ** 9 + 7)

test = Solution()
print test.numSub("0110111")
print test.numSub("101")
print test.numSub("111111")
print test.numSub("000")
print test.numSub("1")