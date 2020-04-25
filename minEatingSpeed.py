class Solution(object):
    def minEatingSpeed(self, piles, H):
        left = min(piles)
        right = max(piles)
        while left + 1 < right:
            mid = (left + right) / 2
            if self.finish(piles[:], mid) <= H:
                right = mid
            else:
                left = mid
        if self.finish(piles, left) <= H:
            return left
        else:
            return right

    def finish(self, piles, n):
        cnt = 0
        while len(piles) != 0:
            cnt += 1
            curr = piles.pop(0)
            curr -= n
            if curr > 0:
                piles.append(curr)
        return cnt

test = Solution()
print test.minEatingSpeed([3,6,7,11], 8)
print test.minEatingSpeed([30,11,23,4,20], 5)
print test.minEatingSpeed([30,11,23,4,20], 6)
# print test.finish([3,6,7,11], 4)