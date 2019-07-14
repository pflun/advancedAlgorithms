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
            if v > len(S) / 2:
                return ""
            heapq.heappush(heap, (v, k))

        while len(heap) >= 2:
            v1, k1 = heapq.heappop(heap)
            v2, k2 = heapq.heappop(heap)
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
