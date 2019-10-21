# https://www.youtube.com/watch?v=r6I-ikllNDM
# DP
class Solution(object):
    def canPartition(self, nums):
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2
        exist = set([0])
        for n in nums:
            tmp = []
            for v in exist:
                tmp.append(n + v)
            for t in tmp:
                exist.add(t)
            if target / 2 in exist:
                return True
        return False

test = Solution()
print test.canPartition([1, 5, 11, 5])
print test.canPartition([1, 2, 3, 5])