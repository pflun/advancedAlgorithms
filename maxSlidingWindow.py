# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=3w8kGAsBxYQ
class Solution(object):
    # brutal force
    def maxSlidingWindow(self, nums, k):
        if not nums or not k:
            return []
        res = []
        window = nums[:k]
        res.append(max(window))
        for num in nums[k:]:
            window.pop(0)
            window.append(num)
            res.append(max(window))

        return res

    # liner solution, deque store index (instead of value) deque内部value从大到小排序
    # 这个解法挺取巧
    def maxSlidingWindow2(self, nums, k):
        res = []
        deque = []
        for i in range(len(nums)):
            # deque首是最大值且滑动窗口移走（该删除）
            if deque and deque[0] == i - k:
                deque.pop(0)
            # curr更大则删除之前较小的，所做的一切都是为了deque内部降序（所以很容易得到瞬时最大值）
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)
            # res的长度不大于nums的长度
            if i + 1 >= k:
                res.append(nums[deque[0]])
        return res


test = Solution()
print test.maxSlidingWindow2([1,3,-1,-3,5,3,6,7], 3)