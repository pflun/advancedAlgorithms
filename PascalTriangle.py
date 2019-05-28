class Solution(object):
    def generate(self, numRows):
        n, b, res = 0, [1], []
        while n < numRows:
            res.append(b)
            b = [1] + [b[i] + b[i + 1] for i in range(len(b) - 1)] + [1]
            n += 1
            print b
        return res

test = Solution()
print test.generate(2)

