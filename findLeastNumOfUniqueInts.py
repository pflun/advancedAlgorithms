import heapq
class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        dic = {}
        heap = []
        heapq.heapify(heap)
        for a in arr:
            dic[a] = dic.get(a, 0) + 1
        for key, val in dic.items():
            heapq.heappush(heap, [val, key])
        while k > 0:
            currv, currk = heapq.heappop(heap)
            currv -= 1
            if currv > 0:
                heapq.heappush(heap, [currv, currk])
            k -= 1
        return len(heap)

test = Solution()
print test.findLeastNumOfUniqueInts([5,5,4], 1)
print test.findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3)