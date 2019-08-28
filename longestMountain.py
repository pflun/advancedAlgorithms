# -*- coding: utf-8 -*-
# 給一組int array [1, 2, 3, 4, 2]
# 找最長的 "山"長度, 山的定義是指 先數組上升在下降
# 在這個case就是 1, 2, 3, 4, 2
# ex2: [1, 2, 1, 3, 1]的話 答案是 3
class Solution(object):
    def longestMountain(self, arr):
        res = 0
        up = []
        down = []
        tmpUp = 0
        tmpDown = 0
        for i in range(len(arr) - 1):
            if arr[i + 1] >= arr[i]:
                tmpUp += 1
                if tmpDown != 0:
                    down.append(tmpDown)
                    tmpDown = 0
            else:
                tmpDown += 1
                if tmpUp != 0:
                    up.append(tmpUp)
                    tmpUp = 0
        if tmpDown != 0:
            down.append(tmpDown)

        # 如果一开始是downhill的话，要验证一下然后从down里pop（0）出去，同理结尾uphill

        for i in range(len(up)):
            res = max(res, up[i] + down[i])

        return res

    def longestMountain2(self, A):
        up = [0]
        down = [0]
        tmpUp = 0
        tmpDown = 0
        res = 0
        for i in range(len(A) - 1):
            if A[i + 1] >= A[i]:
                tmpUp += 1
            else:
                tmpUp = 0
            up.append(tmpUp)

        for i in range(len(A) - 1, 0, -1):
            if A[i] <= A[i - 1]:
                tmpDown += 1
            else:
                tmpDown = 0
            down = [tmpDown] + down

        for i in range(len(A) - 1):
            res = max(res, up[i] + down[i])
        return res + 1

test1 = Solution()
print test1.longestMountain2([1, 2, 3, 2, 1, 3, 1])