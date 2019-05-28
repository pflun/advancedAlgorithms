# -*- coding: utf-8 -*-
# max: https://www.youtube.com/watch?v=3w8kGAsBxYQ
class Solution(object):
    # liner solution, deque store index (instead of value) deque内部value从小到大排序
    # 这个解法挺取巧
    def minSlidingWindow(self, nums, k):
        res = []
        deque = []
        for i in range(len(nums)):
            # deque首是最大值且滑动窗口移走（该删除）
            if deque and deque[0] == i - k:
                deque.pop(0)
            # curr更小则删除之前较大的，所做的一切都是为了deque内部降序（所以很容易得到瞬时最小值）
            while deque and nums[deque[-1]] > nums[i]:
                deque.pop()
            deque.append(i)
            # res的长度不大于nums的长度
            if i + 1 >= k:
                res.append(nums[deque[0]])
            # print deque, '          ', res
        return res


test = Solution()
print test.minSlidingWindow([1,3,-1,-3,5,3,6,7], 3)