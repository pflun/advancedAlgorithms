class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        res = k
        dic = {}
        left = 0
        right = 0
        while right < len(s):
            dic[s[right]] = dic.get(s[right], 0) + 1
            while len(dic) > k:
                dic[s[left]] = dic.get(s[left]) - 1
                if dic[s[left]] == 0:
                    dic.pop(s[left])
                left += 1

            if len(dic) == k:
                res = max(res, right - left + 1)

            right += 1

        return res

test = Solution()
print test.lengthOfLongestSubstringKDistinct("eceba", 2)