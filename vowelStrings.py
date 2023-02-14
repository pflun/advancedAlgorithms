# -*- coding: utf-8 -*-
class Solution(object):
    def vowelStrings(self, words, queries):
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        total = 0
        preSum = [0]
        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                preSum.append(preSum[-1] + 1)
                total += 1
            else:
                preSum.append(preSum[-1])
        res = []
        for q in queries:
            # 因为preSum 1位置是words[0]，那么preSum[q[0]]位置就用来计算不包含q[0]的左端
            left_end = preSum[q[0]]
            # 这里计算右端加1，把preSum打印出来用一个例子带进去就知道需要+1
            right_end = total - preSum[q[1] + 1]
            # 中间部分 = 总数 - 左侧累积 - 右侧累计
            res.append(total - left_end - right_end)
        return res


test = Solution()
print test.vowelStrings(["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]])
print test.vowelStrings(["a","e","i"], [[0,2],[0,1],[2,2]])
print test.vowelStrings(["aba","bcb","ece","aa","e"], [[0,0]])