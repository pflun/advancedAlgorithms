# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=95FNN8210lY
# all element in right child must larger than root, keep update root (min)

class Solution(object):
    def verifyPreorder(self, preorder):
        # stackbaocun路径上可能的root
        stack = []
        min = -float("inf")

        for num in preorder:
            # check if element in right child smaller than root (if so, return false)
            if num < min:
                return False
            # update root (min) when found right child
            while stack and num > stack[-1]:
                min = stack.pop()
            # 当前节点作为路径上可能的root加入stack（反正会pop覆盖掉如果不是的话）
            stack.append(num)

        return True

test = Solution()
print test.verifyPreorder([6, 1, 0, 3, 2, 5, 8])
