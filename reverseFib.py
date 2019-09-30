class Solution(object):
    def reverseFib(self, first, second):
        res = [first, second]
        while second > 0:
            tmp = first - second
            res.append(tmp)
            first = second
            second = tmp
        return res

test = Solution()
print test.reverseFib(80, 40)