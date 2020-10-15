# btw we do not need more than 3 letters to build a non-repeating character sequence, so a b c should be good
from string import ascii_lowercase
class Solution(object):
    def modifyString(self, s):
        res = ''
        for i in range(len(s)):
            if s[i] == '?':
                if i == 0:
                    prev = None
                else:
                    prev = res[-1]
                if i == len(s) - 1:
                    next = None
                else:
                    next = s[i + 1]
                for c in ascii_lowercase:
                    if c != prev and c != next:
                        res += c
                        break
            else:
                res += s[i]
        return res

test = Solution()
print test.modifyString("?zs")
print test.modifyString("ubv?w")
print test.modifyString("j?qg??b")
print test.modifyString("??yw?ipkj?")