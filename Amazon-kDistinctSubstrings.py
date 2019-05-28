# -*- coding: utf-8 -*-

class Solution(object):
    def kDistinctSubstrings(self, string, k):
        if len(string) < k:
            return []
        res = []
        for i in range(k, len(string)):
            if len(set(string[i - k:i])) == k:
                res.append(string[i - k:i])

        return res

    def kMinus1DistinctSubstrings(self, string, k):
        if len(string) < k:
            return []
        res = []
        for i in range(k, len(string)):
            if len(set(string[i - k:i])) == k - 1:
                res.append(string[i - k:i])

        return res


test = Solution()
print test.kDistinctSubstrings('awaglknagawunagwkwagl', 4)
print test.kMinus1DistinctSubstrings('awaglknagawunagwkwagl', 4)