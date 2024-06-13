# -*- coding: utf-8 -*-
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

    # binarySearchTemplate.py
    def minEatingSpeed2(self, piles, H):
        l = 0
        r = max(piles) + 1
        while l < r:
            # 搜索吃香蕉速度
            m = (l + r) / 2
            # 计算当前速度下吃完要多久
            # 每pile吃多少小时，有余就+1小时
            h = 0
            for p in piles:
                div = p / m
                h += div
                if p % m != 0:
                    h += 1

            if h <= H: # 可以吃完
                r = m
            else:
                l = m + 1
        # 找到最小速度满足吃完
        return l

test = Solution()
print test.minEatingSpeed2([3,6,7,11], 8)
print test.minEatingSpeed2([30,11,23,4,20], 5)
print test.minEatingSpeed2([30,11,23,4,20], 6)
# print test.finish([3,6,7,11], 4)