# -*- coding: utf-8 -*-
import heapq
class Solution(object):
    # 快速获取滑动窗口内部的“最大值”和“最小值”
    def longestSubarray2(self, nums, limit):
        max_heap = [] # 存 (-val, index)，Python 默认是最小堆，存负值变最大堆
        min_heap = [] # 存 (val, index)
        l = 0
        res = 0
        for r in range(len(nums)):
            # 1. 右指针元素无脑进堆
            heapq.heappush(max_heap, (-nums[r], r))
            heapq.heappush(min_heap, (nums[r], r))
            # 2. 如果当前窗口的最大值和最小值之差超过 limit，说明窗口不合法了
            while -max_heap[0][0] - min_heap[0][0] > limit:
                l += 1
                # 3. 延迟删除核心逻辑：
                # 看看当前堆顶的“老大”是不是已经不在窗口里了（过期了）
                # 如果过期了，就把它踢掉，让下一个合法的老大浮上来
                # 不在堆顶的不用删，反正它也不是最小的，不影响快速获取“最大值”和“最小值”
                while max_heap[0][1] < l:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < l:
                    heapq.heappop(min_heap)
            res = max(res, r - l + 1)
        return res

    # "Absolute difference between any two elements is less than or equal to limit" is basically => "Absolute difference between min and max elements of subarray"
    # two pointer, maxQueue保持降序，minQueue保持升序
    def longestSubarray(self, nums, limit):
        res = 1
        maxQueue = []
        minQueue = []
        l = 0
        r = 0
        while r < len(nums):
            # update maxQueue
            while len(maxQueue) != 0 and maxQueue[-1] < nums[r]:
                maxQueue.pop()
            maxQueue.append(nums[r])

            # update minQueue
            while len(minQueue) != 0 and minQueue[-1] > nums[r]:
                minQueue.pop()
            minQueue.append(nums[r])

            # move left pointer
            while maxQueue[0] - minQueue[0] > limit:
                if maxQueue[0] == nums[l]:
                    maxQueue.pop(0)
                if minQueue[0] == nums[l]:
                    minQueue.pop(0)
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res


test = Solution()
print test.longestSubarray([8,2,4,7], 4)