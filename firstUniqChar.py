class Solution(object):
    def firstUniqChar(self, s):
        if len(s) == 0:
            return -1

        # OrderedDict keep the order when adding element into dict
        from collections import OrderedDict
        dic = OrderedDict()

        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i], 0) + 1

        for key, val in dic.items():
            if val == 1:
                break

        for i in range(len(s)):
            if s[i] == key:
                return i

        return -1

test = Solution()
print test.firstUniqChar("aabbcdeef")