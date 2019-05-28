# -*- coding: utf-8 -*-
# 先用end找包含短串的最右端，start再走找最左端, sum == 0 代表是否子串完全包含短串
class Solution(object):
    def subSequenceTags(self, targetList, availableTagList):
        if len(targetList) == 0 or len(availableTagList) == 0:
            return [0]

        res = []
        dic = {}
        for tag in targetList:
            tag = tag.lower()
            dic[tag] = dic.get(tag, 0) + 1

        start = 0
        end = 0
        rStart = 0
        rEnd = len(availableTagList)
        sum = len(targetList)
        while end < len(availableTagList):
            curr = availableTagList[end].lower()
            end += 1
            dic[curr] = dic.get(curr, 0) - 1

            if dic[curr] >= 0:
                sum -= 1
            # print dic, sum

            while sum == 0:
                # 更新
                if end - start < rEnd - rStart + 1:
                    rStart = start
                    rEnd = end - 1
                curr = availableTagList[start].lower()
                start += 1
                dic[curr] = dic.get(curr, 0) + 1
                if dic[curr] > 0:
                    sum += 1
        res.append(rStart)
        res.append(rEnd)
        return res

test = Solution()
print test.subSequenceTags(["made", "in", "Spain"], ["made", "weather", "forecast", "says", "that", "made", "rain", "in", "spain", "stays"])