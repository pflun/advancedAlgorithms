class Solution(object):
    def equalSubstring2(self, s, t, maxCost):
        self.res = 0
        for j in range(len(s)):
            length = 0
            cost = 0
            for i in range(j, len(s)):
                cost += abs(ord(s[i]) - ord(t[i]))
                if cost > maxCost:
                    break
                length += 1
                self.res = max(self.res, length)

        return self.res

test = Solution()
print test.equalSubstring2("abcd", "bcdf", 3)
print test.equalSubstring2("abcd", "cdef", 3)
print test.equalSubstring2("abcd", "acde", 0)