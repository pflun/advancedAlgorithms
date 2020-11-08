class Solution(object):
    def minDeletions(self, s):
        res = 0
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        freq = []
        for v in dic.values():
            freq.append(v)
        freq.sort(reverse=True)
        used = set()
        for f in freq:
            # print f, used
            if f not in used:
                used.add(f)
            else:
                while f in used:
                    if f == 0:
                        break
                    f -= 1
                    res += 1
                if f != 0:
                    used.add(f)
        return res

test = Solution()
print test.minDeletions("aab")
print test.minDeletions("aaabbbcc")
print test.minDeletions("ceabaacb")
print test.minDeletions("bbcebab")