class Solution(object):
    def minimumLength(self, s):
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        res = 0
        for v in dic.values():
            if v >= 3:
                # after deletion, 3 or 5 => 1 left, 4 => 2 left
                tmp = 1 if v % 2 != 0 else 2
                res += tmp
            else:
                # cannot delete any char
                res += v
        return res

test = Solution()
print test.minimumLength("abaacbcbb")
print test.minimumLength("aa")