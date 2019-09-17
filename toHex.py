class Solution(object):
    def toHex(self, num):
        if num < 0:
            return 'ffffffff'
        elif num == 0:
            return 0
        hex = ['a', 'b', 'c', 'd', 'e', 'f']
        res = ''
        while num > 0:
            curr = num % 16
            if curr >= 10:
                curr = hex[curr % 10]
            else:
                curr = str(curr)
            num /= 16
            res = curr + res
        return res

test = Solution()
print test.toHex(26)