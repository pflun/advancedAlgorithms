class Solution(object):
    def arrayChange(self, nums, operations):
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for o in operations:
            idx = dic[o[0]]
            nums[idx] = o[1]
            del dic[o[0]]
            dic[o[1]] = idx
        return nums

test = Solution()
print test.arrayChange([1,2,4,6], [[1,3],[4,7],[6,1]])
print test.arrayChange([1,2], [[1,3],[2,1],[3,2]])