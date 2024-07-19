class Solution(object):
    def maximumPoints(self, enemyEnergies, currentEnergy):
        if all(e > currentEnergy for e in enemyEnergies):
            return 0
        score = 0
        enemyEnergies.sort()
        markIdx = len(enemyEnergies) - 1
        i = 0
        while i <= markIdx:
            if currentEnergy >= enemyEnergies[i]:
                # Do not need to deduct one by one
                score += currentEnergy / enemyEnergies[i]
                currentEnergy = currentEnergy % enemyEnergies[i]
            else:
                currentEnergy += enemyEnergies[markIdx]
                markIdx -= 1
        return score

test = Solution()
print test.maximumPoints([3,2,2], 2)
print test.maximumPoints([2], 10)
print test.maximumPoints([2], 1)