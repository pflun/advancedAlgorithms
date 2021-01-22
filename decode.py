class Solution(object):
    def decode(self, encoded, first):
        res = [first]
        for e in encoded:
            res.append(e ^ res[-1])
        return res

test = Solution()
print test.decode([1,2,3], 1)
print test.decode([6,2,7,3], 4)