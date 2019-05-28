class Solution(object):
    def reverseString(self, s):
        if len(s) == 0:
            return s
        resList = []

        for i in reversed(s):
            resList.append(i)

        # Different way to reverse
        # for i in range(len(s) - 1, -1, -1):
        #     resList.append(s[i])

        res = ''.join(str(e) for e in resList)
        return res

test = Solution()
print test.reverseString("hello")