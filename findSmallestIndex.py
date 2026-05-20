# You are given an integer array nums of length n and an integer k. Your task is to remove exactly k consecutive elements from nums so that
# the resulting array is balanced, which means the sum of values at even indices equals the sum of values at odd indices.
# Return the smallest starting index of such a k-length consecutive elements to delete
# Example 1:
# Input: nums = [2, 1, 6, 4], k = 1
# Output: 1
# Explanation: Remove the element at index 1 (value 1), resulting in [2, 6, 4], where even indices (0, 2) sum is 2 + 4 = 6, odd indices (1) sum is 6
# Example 2:
# Input: nums = [1, 1, 1, 1, 1, 1], k = 2
# Output: 0

class Solution(object):
    def findSmallestIndex(self, nums, k):
        if k > len(nums):
            return -1
        
        # 1. Calculate total odd and even sums
        total_even = sum(nums[i] for i in range(len(nums)) if i % 2 == 0)
        total_odd = sum(nums[i] for i in range(len(nums)) if i % 2 != 0)
        
        # 2. Setup initial window [0, k-1]
        window_even = sum(nums[i] for i in range(k) if i % 2 == 0)
        window_odd = sum(nums[i] for i in range(k) if i % 2 != 0)
        
        left_even = 0
        left_odd = 0
        
        # Iterate over all possible starting indices for the window
        for i in range(len(nums) - k + 1):
            if i > 0:
                # Update window sums by removing the element that left the window
                # and adding the new element that entered the window
                old_val = nums[i - 1]
                new_val = nums[i + k - 1]
                
                if (i - 1) % 2 == 0:
                    window_even -= old_val
                    left_even += old_val  # What leaves the window goes into the "left" part
                else:
                    window_odd -= old_val
                    left_odd += old_val
                    
                if (i + k - 1) % 2 == 0:
                    window_even += new_val
                else:
                    window_odd += new_val

            # 3. Calculate the "right" sums
            right_even = total_even - left_even - window_even
            right_odd = total_odd - left_odd - window_odd
            
            # 4. Check if the resulting array is balanced based on k's parity
            if k % 2 == 0:
                # Parity does not shift for elements on the right
                if left_even + right_even == left_odd + right_odd:
                    return i
            else:
                # Parity shifts for elements on the right (even becomes odd, odd becomes even)
                if left_even + right_odd == left_odd + right_even:
                    return i
                    
        return -1

test = Solution()
print(test.findSmallestIndex([2, 1, 6, 4], 1))
print(test.findSmallestIndex([1, 1, 1, 1, 1, 1], 2))
print(test.findSmallestIndex([1, 2, 3], 1))