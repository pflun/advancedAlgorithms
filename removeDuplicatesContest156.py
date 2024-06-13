# Contest 156, 5206
# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation:
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"

class Solution(object):
    # https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/solutions/2012318/python-simple-one-pass-solution/
    def removeDuplicates2(self, s, k):
        stck = [['$', 0]]  # a placeholder to mark stack is empty. This eliminates the need to do an empty check later

        for c in s:
            if stck[-1][0] == c:
                stck[-1][1] += 1  # update occurences count of top element if it matches current character
                if stck[-1][1] == k:
                    stck.pop()
            else:
                stck.append([c, 1])

        return ''.join(c * cnt for c, cnt in stck)

    # Bug
    def removeDuplicates(self, s, k):
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[i] == s[j]:
                j += 1
            if j - i >= k:
                s = s[:i] + s[j:]
                i = 0
            else:
                i += 1
        return s

test = Solution()
print test.removeDuplicates2("deeedbbcccbdaa", 3)