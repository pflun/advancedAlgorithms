# 1100. Find K-Length Substrings With No Repeated Characters
from collections import defaultdict
class Solution(object):
    def numKLenSubstrNoRepeats(self, s, k):
        if len(s) < k:
            return 0
        dic = defaultdict(int)
        for i in range(k):
            dic[s[i]] = dic.get(s[i], 0) + 1
        res = 1 if len(dic) == k else 0
        for i in range(k, len(s)):
            dic[s[i - k]] = dic.get(s[i - k]) - 1
            if dic[s[i - k]] == 0:
                del dic[s[i - k]]
            dic[s[i]] = dic.get(s[i], 0) + 1
            if len(dic) == k:
                res += 1
        return res

test = Solution()
print test.numKLenSubstrNoRepeats("havefunonleetcode", 5)