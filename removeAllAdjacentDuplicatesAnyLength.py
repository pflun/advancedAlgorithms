# Leetcode 1047 (2 adjacent) and 1209 (k adjacent), here we're solving any adjacent
# "abbba" -> "aa" -> ""
# "ab" -> "ab"

class Solution(object):
    def removeDuplicates(self, s):
        stck = [['$', 0]]  # a placeholder to mark stack is empty. This eliminates the need to do an empty check later

        for c in s:
            if stck[-1][0] == c:
                stck[-1][1] += 1  # update occurences count of top element if it matches current character
            else:
                if stck[-1][1] >= 2:
                    stck.pop()
                if stck[-1][0] == c:
                    stck.pop()
                else:
                    stck.append([c, 1])

        if stck[-1][1] >= 2:
            stck.pop()

        res = ''
        for c, cnt in stck[1:]:
            res += c

        return res

test = Solution()
print test.removeDuplicates("abbba")
print test.removeDuplicates("acbbbcaade")