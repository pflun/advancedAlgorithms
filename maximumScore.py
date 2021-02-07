import heapq
class Solution(object):
    def maximumScore(self, a, b, c):
        res = 0
        arr = [a, b, c]
        arr.sort()
        small = arr[0]
        large = arr[2]
        mid = arr[1]
        if small + mid > large:
            while small + mid > large:
                res += 1
                small -= 1
                mid -= 1
            return res + small + mid
        else:
            return small + mid

    # wrong
    def maximumScore2(self, a, b, c):
        res = 0
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, -a)
        heapq.heappush(heap, -b)
        heapq.heappush(heap, -c)
        while len(heap) > 1:
            large = -heapq.heappop(heap)
            small = -heapq.heappop(heap)
            print large, small
            res += min(large, small)
            remain = large - small
            if remain > 0:
                heapq.heappush(heap, -remain)
        return res

test = Solution()
print test.maximumScore(2, 4, 6)
print test.maximumScore(4, 4, 6)
print test.maximumScore(1, 8, 8)