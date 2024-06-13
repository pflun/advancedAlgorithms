class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        dic = {}
        left = 0
        right = 0
        res = 0
        while right < len(s):
            dic[s[right]] = dic.get(s[right], 0) + 1
            if len(dic) <= 2:
                res = max(res, right - left + 1)
            else:
                while len(dic) > 2:
                    dic[s[left]] -= 1
                    if dic[s[left]] == 0:
                        del dic[s[left]]
                    left += 1
            right += 1
        return res