# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=l8_vcmjQA4g
# binary search 找在dic[当前搜索的字符]第一个大于等于idx的位置，找不到就不匹配，找到了更新idx
class Solution(object):
    def numMatchingSubseq(self, S, words):
        dic = {}
        res = 0
        for i in range(len(S)):
            dic[S[i]] = dic.get(S[i], []) + [i]

        # binary search找第一个比目标大的数，没有就返回None
        def search(idx, c):
            low, high = 0, len(dic[c]) - 1
            while low < high:
                mid = (low + high) / 2
                if dic[c][mid] <= idx:
                    low = mid + 1
                else:
                    high = mid
            if dic[c][low] > idx:
                return dic[c][low]
            else:
                return None

        for w in words:
            # -1是因为第一个比-1大的是0
            idx = -1
            for i in range(len(w)):
                if w[i] in dic:
                    idx = search(idx, w[i])
                    if idx is None:
                        break
                else:
                    break
                if i == len(w) - 1:
                    res += 1

        return res


test = Solution()
print test.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"])