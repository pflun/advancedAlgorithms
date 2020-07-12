class Solution(object):
    def xorOperation(self, n, start):
        arr = [start]
        for i in range(1, n):
            arr.append(start + 2 * i)
        res = start
        for a in arr[1:]:
            res ^= a
        return res

test = Solution()
print test.xorOperation(5, 0)
print test.xorOperation(4, 3)
print test.xorOperation(1, 7)
print test.xorOperation(10, 5)