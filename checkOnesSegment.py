class Solution(object):
    def checkOnesSegment(self, s):
        if len(s) == 1:
            return True
        idx = 1
        while idx < len(s):
            if s[idx] == '0':
                break
            idx += 1
        while idx < len(s):
            if s[idx] == '1':
                return False
            idx += 1
        return True

test = Solution()
print test.checkOnesSegment("1001")
print test.checkOnesSegment("110")