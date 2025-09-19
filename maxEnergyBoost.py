class Solution(object):
    def maxEnergyBoost(self, energyDrinkA, energyDrinkB):
        dpA = [None for _ in range(len(energyDrinkA))]
        dpA[0] = energyDrinkA[0]
        dpB = [None for _ in range(len(energyDrinkB))]
        dpB[0] = energyDrinkB[0]
        for i in range(1, len(energyDrinkA)):
            if i > 1:
                dpA[i] = max(dpA[i - 1], dpB[i - 2]) + energyDrinkA[i]
                dpB[i] = max(dpB[i - 1], dpA[i - 2]) + energyDrinkB[i]
            else:
                dpA[i] = max(dpA[i - 1], 0) + energyDrinkA[i] # technically just dpA[i - 1]
                dpB[i] = max(dpB[i - 1], 0) + energyDrinkB[i]
        return max(dpA[-1], dpB[-1])

test = Solution()
print test.maxEnergyBoost([1,3,1], [3,1,1])
print test.maxEnergyBoost([4,1,1], [1,1,3])