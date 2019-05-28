# -*- coding: utf-8 -*-
# 返回重复超过三次的letter的起点和终点
# Given str = "whaaaaatttsup", return [[2,6],[7,9]].
class Solution(object):
    def twitchWords(self, str):
        prev = ''
        res = []
        cnt = 0
        for i in range(len(str)):
            if str[i] != prev:
                if cnt >= 3:
                    res.append([i - cnt, i - 1])
                cnt = 1
                prev = str[i]
            else:
                cnt += 1

        return res

test = Solution()
print test.twitchWords("whaaaaatttsup")