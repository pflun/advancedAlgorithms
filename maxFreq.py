class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        res = 0
        visited = set()
        for i in range(minSize, maxSize + 1):
            for j in range(len(s) - i + 1):
                if len(set(s[j:j + i])) > maxLetters:
                    continue
                else:
                    if s[j:j + i] in visited:
                        continue
                    visited.add(s[j:j + i])
                    cnt = 1
                    for k in range(j + 1, len(s) - i + 1):
                        if s[j:j + i] == s[k:k + i]:
                            cnt += 1
                    res = max(res, cnt)
        return res

test = Solution()
print test.maxFreq('aababcaab', 2,3,4)
print test.maxFreq('aaaa', 1,3,3)
print test.maxFreq('aabcabcab', 2,2,3)
print test.maxFreq('abcde', 2,3,3)