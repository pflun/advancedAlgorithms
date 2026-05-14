# -*- coding: utf-8 -*-
# You are given an integer array arr of length n, which is a permutation of the integers from 1 to n.
# For every integer k from 1 to n, you need to determine if the numbers from 1 to k form a contiguous subsegment within the array arr.
# A subsegment is defined as a continuous sequence of elements within the array.
# Return a string of length n, where the k-th character (1-indexed) is '1' if the numbers 1 to k are contiguous in arr, and '0' otherwise.
# Example 1:
# Input: arr = [4, 1, 5, 2, 3]
# Output: "10001"
# Explanation:
# - k = 1: The elements from 1 to 1 is just [1]. It appears at index 1. It is contiguous. String = "1"
# - k = 2: The elements from 1 to 2 are [1, 2]. They appear at indices 1 and 3. They are separated by the number 5, so they are not contiguous. String = "10"
# - k = 3: The elements from 1 to 3 are [1, 2, 3]. They appear at indices 1, 3, and 4. They are not contiguous. String = "100"
# - k = 4: The elements from 1 to 4 are [1, 2, 3, 4]. They appear at indices 1, 3, 4, and 0. They are not contiguous. String = "1000"
# - k = 5: The elements from 1 to 5 are [1, 2, 3, 4, 5]. This is the entire array, which is naturally contiguous. String = "10001"
# Example 2:
# Input: arr = [3, 2, 1, 4, 5]
# Output: "11111"
# 维护最小值
class Solution:
    def balancedNumbers(self, arr):
        # idx => val
        dic = {}
        min_val = float('inf')
        max_val = float('-inf')
        for i in range(len(arr)):
            dic[i] = arr[i]
        res = []
        for k in range(len(arr)):
            curr_val = dic[k]
            if curr_val < min_val:
                min_val = curr_val
            if curr_val > max_val:
                max_val = curr_val
            if max_val - min_val == k:
                res.append('1')
            else:
                res.append('0')
        return res

test = Solution()
print test.balancedNumbers([4, 1, 5, 2, 3])
print test.balancedNumbers([3, 2, 1, 4, 5])