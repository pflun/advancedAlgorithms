# -*- coding: utf-8 -*-
# https://www.cnblogs.com/grandyang/p/5586009.html
# 有小bug
import heapq
class Solution(object):
    def rearrangeString(self, str, k):
        res = ''
        length = len(str)
        dic = {}
        heap = []
        heapq.heapify(heap)
        for c in str:
            dic[c] = dic.get(c, 0) + 1
        for k, v in dic.items():
            # v: freq, k:char, 最大堆
            heapq.heappush(heap, (-v, k))

        while heap:
            # heap取出来，用完了freq减一加入tmp，每循环一个k就把用完的tmp加回到heap中
            tmp = []
            i = 0
            while i < min(k, length):
                if len(heap) == 0:
                    return ''
                currFreq, currChar = heapq.heappop(heap)
                res += currChar
                currFreq += 1
                if currFreq < 0:
                    tmp.append((currFreq, currChar))
                i += 1
                length -= 1
            for t in tmp:
                heapq.heappush(heap, t)
        return res

test = Solution()
print test.rearrangeString('aabbcc', 3)
print test.rearrangeString('aaabc', 3)
print test.rearrangeString('aaadbbcc', 2)