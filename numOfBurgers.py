class Solution(object):
    # TLE
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        if tomatoSlices == 0 and cheeseSlices == 0:
            return [0, 0]
        if cheeseSlices == 0:
            return []
        if tomatoSlices / cheeseSlices < 2 or tomatoSlices / cheeseSlices > 4:
            return []
        elif tomatoSlices / cheeseSlices == 4 and tomatoSlices % cheeseSlices > 0:
            return []
        elif tomatoSlices % 2 != 0:
            return []
        for i in range(cheeseSlices + 1):
            if 4 * i + 2 * (cheeseSlices - i) == tomatoSlices:
                return [i, cheeseSlices - i]
        return []

test = Solution()
print test.numOfBurgers(16, 7)
print test.numOfBurgers(17, 4)
print test.numOfBurgers(4, 17)
print test.numOfBurgers(0, 0)
print test.numOfBurgers(2, 1)