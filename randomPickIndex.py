import random
class Solution(object):
    def __init__(self, nums):
        self.dic = {}
        # 3 ==> [2, 3, 4]
        for i in range(len(nums)):
            if nums[i] in self.dic:
                self.dic[nums[i]].append(i)
            else:
                self.dic[nums[i]] = [i]

    def pick(self, target):
        # rand(0 ~ 2)
        index = random.randint(0, len(self.dic[target]) - 1)

        # self.dic[3][index]
        return self.dic[target][index]




obj = Solution([1,2,3,3,3])
print obj.pick(3)