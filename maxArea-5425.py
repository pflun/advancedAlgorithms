class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        horizontalCuts.sort()
        verticalCuts.sort()
        resh = 1
        resw = 1
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        for i in range(1, len(horizontalCuts)):
            th = horizontalCuts[i] - horizontalCuts[i - 1]
            if th > resh:
                resh = th
        for j in range(1, len(verticalCuts)):
            tw = verticalCuts[j] - verticalCuts[j - 1]
            if tw > resw:
                resw = tw
        return resh * resw % (10 ** 9 + 7)

test = Solution()
print test.maxArea(5, 4, [1,2,4], [1,3])
print test.maxArea(5, 4, [3,1], [1])
print test.maxArea(5, 4, [3], [3])