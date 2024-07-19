class Solution(object):
    def maximumLength(self, nums):
        res = 1
        # find odd
        cnt = 0
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                cnt += 1
        res = max(res, cnt)
        # find even
        cnt = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                cnt += 1
        res = max(res, cnt)

        # alternatively odd even
        cnt_odd = self.maximumLengthAlternativeOddEven(nums, 1)
        cnt_even = self.maximumLengthAlternativeOddEven(nums, 0)
        res = max(res, cnt_odd)
        res = max(res, cnt_even)
        return res

    def maximumLengthAlternativeOddEven(self, nums, flag):
        # find first odd or even
        i = 0
        while i < len(nums):
            if nums[i] % 2 == flag:
                break
            i += 1
        cnt = 1
        next = flag
        for j in range(i + 1, len(nums)):
            if nums[j] % 2 == 1 - next:
                cnt += 1
                next = 1 - next
            else:
                continue
        return cnt

test = Solution()
print test.maximumLength([1,2,3,4])
print test.maximumLength([1,2,1,1,2,1,2])
print test.maximumLength([1,3])