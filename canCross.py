# https://www.youtube.com/watch?v=-FBfrVz841k
class Solution(object):
    def canCross(self, stones):
        if len(stones) <= 1:
            return True
        dic = {}
        # stone index => [lastSteps]
        for stone in stones:
            dic[stone] = set([])
        dic[0].add(0)

        for stone in stones:
            for lastStep in dic[stone]:
                for nextStep in [lastStep - 1, lastStep, lastStep + 1]:
                    if nextStep > 0 and stone + nextStep in dic:
                        dic[stone + nextStep].add(nextStep)

        return True if len(dic[stones[-1]]) != 0 else False

test = Solution()
print test.canCross([0,1,3,5,6,8,12,17])