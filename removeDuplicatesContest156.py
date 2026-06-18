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
        # [[char, cnt]]
        stack = []
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            else:
                stack[-1][1] += 1  # update occurences count of top element if it matches current character
                if stack[-1][1] == k:
                    stack.pop()

        return ''.join(c * cnt for c, cnt in stack)

test = Solution()
print test.removeDuplicates2("deeedbbcccbdaa", 3)