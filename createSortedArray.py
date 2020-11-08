class Solution(object):
    # TLE
    def createSortedArray(self, instructions):
        nums = []
        cost = 0
        dic = {}
        for a in instructions:
            if len(nums) == 0:
                nums.append(a)
                dic[a] = 1
            else:
                for i in range(len(nums)):
                    if i == len(nums) - 1 and nums[-1] < a:
                        dic[a] = dic.get(a, 0) + 1
                        nums.append(a)
                        break
                    if nums[i] >= a:
                        less = i
                        same = dic.get(a, 0)
                        greater = len(nums) - less - same
                        cost += min(less, greater)
                        dic[a] = dic.get(a, 0) + 1
                        nums = nums[:i] + [a] + nums[i:]
                        break
        return cost % (10 ** 9 + 7)

test = Solution()
print test.createSortedArray([1,5,6,2])
print test.createSortedArray([1,2,3,6,5,4])
print test.createSortedArray([1,3,3,3,2,4,2,1,2])