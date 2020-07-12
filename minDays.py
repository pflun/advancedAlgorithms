class Solution(object):
    def minDays(self, bloomDay, m, k):
        if len(bloomDay) < m * k:
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        while low + 1 < high:
            mid = (low + high) / 2
            if not self.helper(bloomDay, m, k, mid):
                low = mid
            else:
                high = mid
        if self.helper(bloomDay, m, k, low):
            return low
        else:
            return high

    def helper(self, bloomDay, m, k, target):
        copy = bloomDay[:]
        for i in range(len(copy)):
            if copy[i] > target:
                copy[i] = None
        i = 0
        cnt = 0
        while i < len(copy):
            if not copy[i]:
                cnt = 0
            if copy[i]:
                cnt += 1
            if cnt == k:
                m -= 1
                if m == 0:
                    return True
                cnt = 0
            i += 1
        return False

test = Solution()
print test.minDays([1,10,3,10,2], 3, 1)
print test.minDays([1,10,3,10,2], 3, 2)
print test.minDays([7,7,7,7,12,7,7], 2, 3)
print test.minDays([1000000000,1000000000], 1, 1)
print test.minDays([1,10,2,9,3,8,4,7,5,6], 4, 2)