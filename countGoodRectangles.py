class Solution(object):
    def countGoodRectangles(self, rectangles):
        res = []
        for r in rectangles:
            res.append(min(r[0], r[1]))
        maxLen = max(res)
        cnt = 0
        for r in res:
            if r == maxLen:
                cnt += 1
        return cnt

test = Solution()
print test.countGoodRectangles([[5,8],[3,9],[5,12],[16,5]])
print test.countGoodRectangles([[2,3],[3,7],[4,3],[3,7]])