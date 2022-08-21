# -*- coding: utf-8 -*-
class Solution(object):
    def minimumCardPickup(self, cards):
        res = float('inf')
        l = 0
        r = 0
        pickup = set()
        while r < len(cards):
            if cards[r] not in pickup:
                pickup.add(cards[r])
                r += 1
            else:
                # 左指针挪到第一次遇见cards[r]的值的位置
                while l < r and cards[l] != cards[r]:
                    pickup.remove(cards[l])
                    l += 1
                res = min(res, r - l + 1)
                # 删左cards[l]增右cards[r]，但是两边一样就不删(也不加)了
                l += 1
                # 右cards[r]增了所以++
                r += 1
        return res if res != float('inf') else -1

test = Solution()
print test.minimumCardPickup([3,4,2,3,4,7])
print test.minimumCardPickup([1,0,5,3])
print test.minimumCardPickup([95,11,8,65,5,86,30,27,30,73,15,91,30,7,37,26,55,76,60,43,36,85,47,96,6]) # Expected: 3
