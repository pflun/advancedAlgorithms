class Solution(object):
    def maximumEnergy(self, energy, k):
        dp = []
        for i in range(k):
            dp.append(energy[i])
        for i in range(k, len(energy)):
            maxEnergy = max(energy[i], energy[i] + dp[i - k])
            dp.append(maxEnergy)
        return max(dp[len(energy) - k:])

test = Solution()
print test.maximumEnergy([5,2,-10,-5,1], 3)
print test.maximumEnergy([-2,-3,-1], 2)
print test.maximumEnergy([-8,10,-10], 1)