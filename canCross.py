# https://www.youtube.com/watch?v=-FBfrVz841k
class Solution(object):
    def canCross2(self, stones):
        if len(stones) <= 1:
            return True
        dic = {}
        # stone index => [lastSteps]
        for i in range(len(stones)):
            dic[i] = set([])
        dic[0].add(0)

        for i in range(len(stones)):
            for lastStep in dic[i]:
                for nextStep in [lastStep - 1, lastStep, lastStep + 1]:
                    if nextStep > 0 and stones[i] + nextStep in dic:
                        dic[stones[i] + nextStep].add(nextStep)

        return True if len(dic[len(stones) - 1]) != 0 else False

test = Solution()
print test.canCross([0,1,3,5,6,8,12,17])