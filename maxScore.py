class Solution(object):
    def maxScore(self, s):
        zeros = [0]
        ones = [0]
        for c in s:
            if c == '0':
                zeros.append(zeros[-1] + 1)
            else:
                zeros.append(zeros[-1])
        for c in s[::-1]:
            if c == '1':
                ones = [1 + ones[0]] + ones
            else:
                ones = [ones[0]] + ones
        res = 0
        for i in range(1, len(zeros) - 1):
            res = max(res, zeros[i] + ones[i])
        return res

test = Solution()
print test.maxScore("011101")
print test.maxScore("00111")
print test.maxScore("1111")
print test.maxScore("1")
print test.maxScore("11")