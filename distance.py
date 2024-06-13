class Solution(object):
    # TLE, should optimize: z - x + z - y = 2z - (x + y) = (count) * (currentIndex) - (sum).
    def distance(self, nums):
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = []
            dic[nums[i]].append(i)
        res = []
        for i in range(len(nums)):
            same = dic[nums[i]]
            tmp = 0
            for s in same:
                if s != i:
                    tmp += abs(i - s)
            res.append(tmp)
        return res