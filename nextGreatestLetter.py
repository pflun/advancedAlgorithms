# LC 744
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        low, high = 0, len(letters) - 1

        while low < high:
            mid = low + (high - low) // 2
            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid

        # If not found, return None. i.e. [2, 4, 6], target = 7
        if letters[low] > target:
            return letters[low]
        else:
            return None