class Solution(object):
    def kLengthApart(self, nums, k):
        last = None
        for i in range(len(nums)):
            if nums[i] == 1:
                if not last:
                    last = i
                    continue
                else:
                    if i - last >= k + 1:
                        last = i
                        continue
                    else:
                        return False
        return True