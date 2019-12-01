# -*- coding: utf-8 -*-
# https://leetcode.com/problems/hand-of-straights/discuss/425060/Python-(96.6-runtime-100-memory)-w-intuition-and-comments
# each group is exact size W
from collections import Counter
class Solution(object):
    def isNStraightHand(self, hand, W):
        hand.sort()
        counter = Counter(hand)

        for i in range(len(hand)):
            # hand[i]必须没有被用掉
            if counter[hand[i]] > 0:
                # 尝试把start with hand[i]的新组fill W个，看是否成功
                for j in range(hand[i], hand[i] + W):
                    if counter[j] > 0:
                        counter[j] -= 1
                    else:
                        return False

        return True

test = Solution()
print test.isNStraightHand([1,2,3,6,2,3,4,7,8], 3)