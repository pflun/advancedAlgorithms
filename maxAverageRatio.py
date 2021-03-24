# -*- coding: utf-8 -*-
import heapq
class Solution(object):
    # key应该是加一个学生能增加的通过率
    def maxAverageRatio(self, classes, extraStudents):
        heap = []
        heapq.heapify(heap)
        for c in classes:
            heapq.heappush(heap, [-self.profit(c[0], c[1]), c[0], c[1]])
        for _ in range(extraStudents):
            curr = heapq.heappop(heap)
            heapq.heappush(heap, [-self.profit(curr[1] + 1, curr[2] + 1), curr[1] + 1, curr[2] + 1])

        res = float(0)
        for a in heap:
            res += float(a[1]) / a[2]
        return round(res / len(classes), 5)

    # 1个学生增加的通过率
    def profit(self, pas, total):
        return float(pas + 1) / (total + 1) - float(pas) / total

test = Solution()
print test.maxAverageRatio([[1,2],[3,5],[2,2]], 2)
print test.maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 4)
print test.maxAverageRatio([[97,500],[30,915],[400,856],[444,623],[781,786],[3,713]], 8) # 0.40288
print test.maxAverageRatio([[222,993],[433,744],[30,541],[228,783],[449,962],[508,567],[239,354],[237,694],[225,780],[471,976]], 7) # 0.43146