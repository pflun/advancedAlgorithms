class Solution(object):
    def pivotIndex(self, nums):
        left = []
        right = []
        for i in range(len(nums) - 1):
            if len(left) == 0:
                left.append(nums[i])
            else:
                left.append(nums[i] + left[i - 1])

        nums = nums[::-1]
        for i in range(len(nums) - 1):
            if len(right) == 0:
                right.append(nums[i])
            else:
                right.append(nums[i] + right[i - 1])

        p1 = 0
        p2 = 0
        while p1 < len(left) and p2 < len(right):
            if left[p1] == right[p2]:
                return p1 + 1
            elif left[p1] < right[p2]:
                p1 += 1
            else:
                p2 += 1
        return -1

test = Solution()
print test.pivotIndex([1, 7, 3, 6, 5, 6])