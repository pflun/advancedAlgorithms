# The essential concepts is you keep a counter for the majority number X. If you find a number Y that is not X, the current counter should deduce 1.
# The reason is that if there is 5 X and 4 Y, there would be one (5-4) more X than Y. This could be explained as "4 X being paired out by 4 Y".
# And since the requirement is finding the majority for more than ceiling of [n/3], the answer would be less than or equal to two numbers.
# So we can modify the algorithm to maintain two counters for two majorities.

class Solution(object):
    # Majority Element 2
    def majorityElement(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            print candidate1, count1, candidate2, count2
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                if nums.count(n) > len(nums) // 3]

    # https://leetcode.com/problems/majority-element/description/
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key, val in dic.items():
            if val > len(nums) / 2:
                return key
        return False

test = Solution()
print test.majorityElement([2,2,2,1,5,6,3,3])