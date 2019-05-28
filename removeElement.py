# -*- coding: utf-8 -*-
class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        counter = 0
        B = []
        for i in range(len(A)):
            if A[i] != elem:
                counter += 1
                B.append(A[i])

        return B, counter

    # in-place, ACC
    def removeElement2(self, A, elem):
        i = 0
        size = len(A)
        while i < size:
            if A[i] == elem:
                A.remove(elem)
                # 删除后不增加i因为下一个元素的index就变成了现在的index
                # 删除后，list长度改变，所以更新size
                size -= 1
            else:
                i += 1

        return len(A)

test = Solution()
print test.removeElement2([0,4,4,0,4,4,4,0,2], 4)