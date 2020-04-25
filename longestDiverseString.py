# -*- coding: utf-8 -*-
import heapq
class Solution(object):
    def longestDiverseString(self, a, b, c):
        res = ""
        heap = []
        heapq.heapify(heap)
        if a != 0:
            heapq.heappush(heap, (-a, 'a'))
        if b != 0:
            heapq.heappush(heap, (-b, 'b'))
        if c != 0:
            heapq.heappush(heap, (-c, 'c'))
        while heap:
            currN, currC = heapq.heappop(heap)
            # init
            if len(res) == 0:
                if currN < -1:
                    res += currC + currC
                    currN += 2
                elif currN == -1:
                    res += currC
                    currN += 1
                if currN < 0:
                    heapq.heappush(heap, (currN, currC))
                continue
            # avoid 3 same consecutive as substring, try attach second most
            if len(res) >= 2 and res[-1] == res[-2] == currC:
                # make sure there exist second most
                if len(heap) != 0:
                    nextN, nextC = heapq.heappop(heap)
                    res += nextC
                    nextN += 1
                    if nextN < 0:
                        heapq.heappush(heap, (nextN, nextC))
                    if currN < -1:
                        res += currC + currC
                        currN += 2
                    elif currN == -1:
                        res += currC
                        currN += 1
                    if currN < 0:
                        heapq.heappush(heap, (currN, currC))
                    continue
                # no second most exists, you don't have other choice so just return
                else:
                    return res
            # general case, attach most element
            if currN < -1:
                res += currC + currC
                currN += 2
            elif currN == -1:
                res += currC
                currN += 1
            if currN < 0:
                heapq.heappush(heap, (currN, currC))
        return res


test = Solution()
print test.longestDiverseString(1,1,7)
print test.longestDiverseString(2,2,1)
print test.longestDiverseString(7,1,0)
print test.longestDiverseString(2,4,1)