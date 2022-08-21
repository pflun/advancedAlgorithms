import heapq

class Solution(object):
    def maximumImportance(self, n, roads):
        indegree = {}
        heap = []
        importance = [0 for _ in range(n)]
        cnt = n # importance counter, n -> 1
        res = 0
        for r in roads:
            indegree[r[0]] = indegree.get(r[0], 0) + 1
            indegree[r[1]] = indegree.get(r[1], 0) + 1
        for i in range(n):
            if i not in indegree:
                indegree[i] = 0
        heapq.heapify(heap)
        for k, v in indegree.items():
            heapq.heappush(heap, [-v, k])
        while heap:
            curr = heapq.heappop(heap)
            # blindly assign importance from n to 1
            importance[curr[1]] = cnt
            cnt -= 1
        for r in roads:
            res += importance[r[0]] + importance[r[1]]
        return res

test = Solution()
print test.maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]])
print test.maximumImportance(5, [[0,3],[2,4],[1,3]])
# Solution2, instead of using heap, reverse sort by indegree would also work.