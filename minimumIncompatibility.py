import heapq
# bug, incorrect
class Solution(object):
    def minimumIncompatibility(self, nums, k):
        if len(nums) % 4 != 0:
            return -1
        target = len(nums) / k
        res = [[] for _ in range(k)]
        heap = nums
        heapq.heapify(heap)
        prevVal = None
        prevBucket = 0
        while heap:
            curr = heapq.heappop(heap)
            if curr != prevVal:
                if len(res[prevBucket]) < target:
                    res[prevBucket].append(curr)
                else:
                    while len(res[prevBucket]) >= target:
                        prevBucket += 1
                        prevBucket %= k
                    res[prevBucket].append(curr)
                prevVal = curr
            else:
                prevBucket += 1
                prevBucket %= k
                if len(res[prevBucket]) < target:
                    res[prevBucket].append(curr)
                else:
                    while len(res[prevBucket]) >= target:
                        prevBucket += 1
                        prevBucket %= k
                    res[prevBucket].append(curr)
                prevVal = curr
        rnt = 0
        for r in res:
            maxVal = max(r)
            minVal = min(r)
            rnt += maxVal - minVal
        return rnt, res


test = Solution()
print test.minimumIncompatibility([1,2,1,4], 2)
print test.minimumIncompatibility([6,3,8,1,3,1,2,2], 4)
print test.minimumIncompatibility([5,3,3,6,3,3], 3)