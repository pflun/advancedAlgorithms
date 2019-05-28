class Solution(object):
    def findDuplicates(self, nums):
        # Hash, with extra space
        # dic = {}
        # for i in nums:
        #     dic[i] = dic.get(i, 0) + 1
        # for key, val in dic.items():
        #     if val == 2:
        #         return key

        # Sort is nlogn
        # res = []
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i + 1] == nums[i]:
        #         res.append(nums[i])
        # return res

        # map val n to index n - 1, when first meet val n, set num[n - 1] to negative, when second meet val n, check if num[n - 1] is negative
        result = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                result.append(abs(x))
            else:
                nums[abs(x) - 1] = -1 * nums[abs(x) - 1]
        return result

test = Solution()
print test.findDuplicates([4,3,2,7,8,2,3,1])