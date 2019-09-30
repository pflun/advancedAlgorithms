# Contest 156, 5206
# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation:
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"

class Solution(object):
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
print test.removeDuplicates("deeedbbcccbdaa", 3)