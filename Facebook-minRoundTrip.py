# -*- coding: utf-8 -*-
# 给往返机票依据天数的价格：
# 去程：
# [10 6 3 7]
# 回程
# [3 8 9 10]
# 让你求最小的往返票组合，回程天数得大于或等于去程。
# 这题的意思就是，去程昨天3今天4，对于4这个点来说买昨天的票就行了，但是不能买明天的票会影响计算
# 同理对于去程，买买晚一天的票不影响计算，但是买前一天的票会冲突
# arr1找到去程方向的最小值，arr2倒着找回程的
class Solution(object):
    def minRoundTrip(self, depart, back):
        arr1 = []
        arr2 = []
        for i in range(len(depart)):
            if len(arr1) == 0:
                arr1.append(depart[i])
            else:
                arr1.append(min(arr1[i - 1], depart[i]))

        back = back[::-1]
        for j in range(len(back)):
            if len(arr2) == 0:
                arr2.append(back[j])
            else:
                arr2.append(min(arr2[j - 1], back[j]))
        arr2 = arr2[::-1]
        res = float('inf')
        for i in range(len(arr1)):
            res = min(res, arr1[i] + arr2[i])
        return res

test = Solution()
print test.minRoundTrip([10,6,3,7], [3,8,9,10])