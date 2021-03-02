# -*- coding: utf-8 -*-
# 用prev暂存这一轮加过的，下一轮再把prev加进heap
import heapq
class Solution(object):
    def reorganizeString(self, S):
        res = ""
        heap = []
        dic = {}
        for s in S:
            dic[s] = dic.get(s, 0) + 1

        heapq.heapify(heap)

        for k, v in dic.items():
            # pruning
            if v > (len(S) + 1) / 2:
                return ""
            heapq.heappush(heap, (v, k))

        # 先加v大的，相等就先加和prev不等的
        while len(heap) >= 2:
            v1, k1 = heapq.heappop(heap)
            v2, k2 = heapq.heappop(heap)
            if v1 > v2:
                res += k1
                res += k2
            elif v2 > v1:
                res += k2
                res += k1
            else:
                if len(res) != 0 and res[-1] == k1:
                    res += k2
                    res += k1
                elif len(res) != 0 and res[-1] == k2:
                    res += k1
                    res += k2
                else:
                    res += k1
                    res += k2
            if v1 - 1 > 0:
                heapq.heappush(heap, (v1 - 1, k1))
            if v2 - 1 > 0:
                heapq.heappush(heap, (v2 - 1, k2))

        if len(heap) > 0:
            v, k = heapq.heappop(heap)
            res += k

        return res

test = Solution()
print test.reorganizeString("aab")
print test.reorganizeString("aaabb")
