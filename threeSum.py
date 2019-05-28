# -*- coding: utf-8 -*-
class Solution(object):
    # two pointer, one from left (after i), the other one from most right
    # 固定一点，从这点下一个开始两头往中间扫，注意去重，相同就跳过
    # 关于去重：https://www.youtube.com/watch?v=gq-uWp327m8
    def threeSum(self, nums):
        nums.sort()
        length = len(nums) - 1
        res = []
        for i in range(length):
            j = i + 1
            k = length
            tmp = []
            # two pointer
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    tmp.extend((nums[i], nums[j], nums[k]))
                    if tmp not in res:
                        res.append(tmp)
                    break
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1

        return res

    # for loop outside twoSum (dict)
    def threeSumWithoutSort(self, nums):
        if len(nums) <= 1:
            return []
        length = len(nums) - 1
        nums.sort()
        res = []
        for i in range(length):
            dict = {}
            for j in range(i, len(nums)):
                # Skip i, otherwise some element will be use twice, ie: [-4, 2, 2]
                if j != i:
                    if nums[j] in dict:
                        # remove duplicated tuple
                        tmp = [nums[i], nums[j], nums[dict[nums[j]]]]
                        # tmp.sort()
                        if tmp not in res:
                            res.append(tmp)
                    else:
                        dict[-nums[i] - nums[j]] = j
        return res

    def threeSum2(self, nums):
        if len(nums) <= 2:
            return []

        nums.sort()
        res = []
        for i in range(len(nums)):
            dic = {}
            for j in range(i, len(nums)):
                if j != i:
                    if - nums[i] - nums[j] in dic:
                        # remove duplicated tuple
                        if [nums[i], nums[j], - nums[i] - nums[j]] not in res:
                            res.append([nums[i], nums[j], - nums[i] - nums[j]])
                    else:
                        dic[nums[j]] = i

        return res


test = Solution()
print test.threeSumWithoutSort([-1, 0, 1, 2, -1, -4])