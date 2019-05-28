class Solution(object):
    def distributeCandies(self, candies):
        dic = {}
        total = len(candies)
        for candy in candies:
            dic[candy] = dic.get(candy, 0) + 1

        if len(dic) <= total / 2:
            # If kinds less than half numbers, you cannot exceed kinds
            return len(dic)
        else:
            # If kinds more than half numbers, simply get each one from each kinds, so there're half numbers kinds
            return total / 2

        return len(dic)

test = Solution()
print test.distributeCandies([1,1,2,3,3,3])