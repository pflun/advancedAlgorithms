class Solution(object):
    def maxTotalReward(self, rewardValues):
        rewardValues = set(rewardValues)
        rewardValues = list(rewardValues)
        rewardValues.sort()
        res = set()
        res.add(0)
        for r in rewardValues:
            new_rewards = set()
            for x in res:
                if r > x:
                    new_rewards.add(x + r)
            res.update(new_rewards)
        return max(res)

test = Solution()
print test.maxTotalReward([1,1,3,3])
print test.maxTotalReward([1,6,4,3,2])