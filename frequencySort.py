import heapq

class Solution(object):
    def negativify(self, n):
        n = -n
        return n

    def frequencySort(self, s):
        res_list = []
        dic = {}
        heap = []
        heapq.heapify(heap)

        # get frequency for each char
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        # add [freq, char] to heap
        for key, val in dic.items():
            heapq.heappush(heap, [self.negativify(val), key])

        while heap:
            tmp = heapq.heappop(heap)
            # append char to list 'freq' times
            for _ in range(self.negativify(tmp[0])):
                res_list.append(tmp[1])

        res = ''.join(res_list)
        return res

test = Solution()
print test.frequencySort('tree')