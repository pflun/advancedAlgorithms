# LC153
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solutions/158940/beat-100-very-simple-python-very-detailed-explanation/?orderBy=most_votes
class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if nums[mid] > nums[right]:
                # rotation part must on the right, so move left to mid+1 (mid already > right)
                left = mid + 1
            else:
                right = mid
        # eventually it would be [left, right] and left < right value
        return nums[left]

# Below solution could be wrong or old
# Looking at subarray with index [start,end]. We can find out that if the first member is less than the last member,
# there's no rotation in the array. So we could directly return the first element in this subarray.
# If the first element is larger than the last one, then we compute the element in the middle, and compare it with the first element.
# If value of the element in the middle is larger than the first element, we know the rotation is at the second half of this array.
# Else, it is in the first half in the array.
class SolutionOld(object):
    def findMin(self, num):
        start = 0
        end = len(num) - 1
        while start < end:
            if num[start] < num[end]:
                # found, because no rotation from start to end
                return num[start]
            mid = (start + end) / 2
            # rotation at right side
            if num[start] < num[end]:
                start = mid
            # rotation at left side
            else:
                end = mid
        return num[start]