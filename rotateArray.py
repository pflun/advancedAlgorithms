# multiple rotate: https://mnmunknown.gitbooks.io/algorithm-notes/content/522_string.html

class Solution(object):
    def rotate(self, nums, k):
        second = nums[k:]
        second.extend(nums[:k])
        return second

    def rotate2(self, nums, k):
        i = 0
        while i < k:
            nums.append(nums.pop(0))
            i += 1
        return nums

test = Solution()
print test.rotate([1,2,3,4,5,6,7], 3)