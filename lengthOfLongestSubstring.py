# -*- coding: utf-8 -*-
# 此题用快慢指针和哈希表 两个指针起始点都一样
# 快指针先开始走 每次把一个元素添加进哈希表里
# 当遇到某个元素在哈希表里已经有了key 说明此时碰见了重复的元素
# 此时就要移动慢指针 每次移动一格 并且把慢指针指向的当前元素从哈希表里删除 直到遇到了重复的那个元素的最先的位置 然后删除掉
# 然后再继续移动快指针
# while fast < len(s):
#     if not str_dict.has_key(s[fast]):
#         str_dict[s[fast]] = 1
#         max_length = max_length if max_length > len(str_dict) else len(str_dict)
#         fast += 1
#     else:
#         str_dict.pop(s[slow])
#         slow += 1

# Brutal force
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        res = 1
        for i in range(len(s)):
            for j in range(i, len(s)):
                dic = {}
                for k in s[i:j + 1]:
                    dic[k] = dic.get(k, 0) + 1
                # if any val == 2, that is, there're repeating characters in string, then tmp won't be equal to len(dic)
                tmp = 0
                for key, val in dic.items():
                    tmp += val
                if tmp == len(dic):
                    res = max(res, tmp)
        return res

    # Need testing
    # https://mnmunknown.gitbooks.io/algorithm-notes/content/614,_two_pointers,_shuang_zhi_zhen_ff0c_chuang_kou.html
    def lengthOfLongestSubstring2(self, s):
        dic = {}
        j = 0
        res = 1
        for i in range(len(s)):
            while j < len(s):
                if s[j] in dic and dic[s[j]] is False:
                    j += 1
                    dic[s[j]] = True
                else:
                    break

            res = max(res, j - i)
            dic[s[i]] = False

        return res

    def lengthOfLongestSubstring3(self, s):
        if len(s) == 0:
            return 0
        left = 0
        right = 1
        res = 1
        hashSet = set(s[0])
        while right < len(s):
            if s[right] in hashSet:
                hashSet.remove(s[left])
                left += 1
            else:
                hashSet.add(s[right])
                right += 1
            res = max(res, len(hashSet))

        return res

test = Solution()
print test.lengthOfLongestSubstring2("abbbb")