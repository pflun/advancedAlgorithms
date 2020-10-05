class Solution(object):
    # backtracking
    def maxUniqueSplit(self, s):

        def helper(s, seen):
            res = 0
            if s:
                for i in range(1, len(s) + 1):
                    candidate = s[:i]
                    if candidate not in seen:
                        seen.add(candidate)
                        res = max(res, 1 + helper(s[i:], seen))
                        seen.remove(candidate)
            return res

        return helper(s, set())

test = Solution()
print test.maxUniqueSplit("ababccc")
print test.maxUniqueSplit("aba")
print test.maxUniqueSplit("aa")