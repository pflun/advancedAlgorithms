import heapq
class Solution(object):
    def kWeakestRows(self, mat, k):
        heap = []
        heapq.heapify(heap)
        for i in range(len(mat)):
            currSum = sum(mat[i])
            heapq.heappush(heap, [-currSum, i])

        dic = {}
        res = []
        while heap:
            curr = heapq.heappop(heap)
            dic[-curr[0]] = dic.get(-curr[0], []) + [curr[1]]
        for i, j in sorted(dic.items()):
            res += j
        return res[:k]

test = Solution()
print test.kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3)
print test.kWeakestRows([[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 2)