# -*- coding: utf-8 -*-
# Single number must have an even index
# 1, 1, 2, 3, 3, 4, 4
# 2之前都是成对的，所以2的index必是偶数
# 更好的方法是binary search （logn）：https://www.youtube.com/watch?v=uJa9Q-05JxY
class Solution(object):
    def singleNonDuplicate(self, list):
        for i in range(0, len(list), 2):
            if list[i] != list[i + 1]:
                return i

test = Solution()
print test.singleNonDuplicate([1,1,2,3,3,4,4,8,8])