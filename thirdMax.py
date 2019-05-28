class Solution(object):
    def thirdMax(self, nums):
        preprocess_set = set(nums)
        if len(preprocess_set) < 3:
            return max(preprocess_set)
        preprocess_set.remove(max(preprocess_set))
        preprocess_set.remove(max(preprocess_set))
        return max(preprocess_set)


class Solution2(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        nums = list(set(nums))
        if len(nums) < 3:
            # return max
            if len(nums) == 1:
                return nums[0]
            elif len(nums) == 2:
                if nums[0] > nums[1]:
                    return nums[0]
                else:
                    return nums[1]

        import heapq
        heap = []
        heapq.heapify(heap)

        for num in nums:
            if len(heap) < 3:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)

        return heap[0]


test = Solution2()
print test.thirdMax([2,2,2,1,3,3,5,6])