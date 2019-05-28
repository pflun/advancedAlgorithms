class Solution(object):
    def fourSum(self, nums, target):
        res = []
        # (str)'set([indexes])' ==> set([indexes])
        dic = {}
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                tmp = self.twoSum(nums, target - nums[i] - nums[j])
                for t in tmp:
                    curr = set([i, j])
                    curr.add(t[0])
                    curr.add(t[1])
                    if len(curr) == 4:
                        # Remove duplicates
                        dic[str(curr)] = curr

        for key, val in dic.items():
            tmp = []
            for v in val:
                tmp.append(nums[v])
            res.append(tmp)

        return res

    def twoSum(self, nums, target):
        dic = {}
        res = []
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[target - nums[i]] = i
            else:
                res.append([dic[nums[i]], i])

        return res

test = Solution()
print test.fourSum([1, 0, -1, 0, -2, 2], 0)