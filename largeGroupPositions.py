class Solution(object):
    def largeGroupPositions(self, S):
        if len(S) < 3:
            return []
        res = []
        cache = [[S[0], 0]]
        for i in range(1, len(S)):
            if len(cache) > 0 and S[i] == cache[-1][0]:
                cache.append([S[i], i])
            else:
                if len(cache) >= 3:
                    res.append([cache[0][1], cache[-1][1]])
                cache = [[S[i], i]]

        # edge case, "aaa"
        if len(cache) >= 3:
            res.append([cache[0][1], cache[-1][1]])

        return res

test = Solution()
print test.largeGroupPositions("abcdddeeeeaabbbcd")