class Solution(object):
    def generateTheString(self, n):
        if n == 0:
            return ''
        res = ''
        if n % 2 == 0:
            res += 'b'
            for _ in range(n - 1):
                res += 'a'
        else:
            for _ in range(n):
                res += 'a'
        return res

test = Solution()
print test.generateTheString(4)
print test.generateTheString(2)
print test.generateTheString(7)
print test.generateTheString(0)
print test.generateTheString(1)