# -*- coding: utf-8 -*-
# https://leetcode.com/problems/combination-sum/discuss/16509/Iterative-Java-DP-solution
# Let's assume sodas are sold in packages of 1, 2, 6, 12, 24
# e.g. if N = 10, you could buy 1 x 10, 6 + 2 + 2, 6 + 1 + 1 + 1 + 1, ....
# input : N
# output : all possible combinations, for instance N=10 { {1,1,...,1}, {6,2,2}, {6,1,1,1,1}, {6,2,1,1}, {2,1,..,1}, .... } (don't include {2,2,6} since we have {6,2,2})
# backtracking and DP solution
# 比如target是6，就是[6] + [2 + dp里所有target = 4 的组合] + 【1 + ...】
# 所以从0开始计算出所有target为1 2 3 4 ... 的组合，当计算到6时，就可以调用前面dp[4]已计算出的组合了
class Solution(object):
    # bug
    def combinationSum(self, N):
        sodas = [1, 2, 6, 12, 24]
        dp = [[] for _ in range(N + 1)]

        for t in range(N + 1):
            tmp = [[]]
            j = 0
            # try all candidates
            while j < len(sodas) and sodas[j] <= t:
                # corner case: 刚好一箱(6, 12...)填满
                if sodas[j] == t:
                    tmp.append([sodas[j]])
                # 填不满，从dp里找，6 = 2 (candidate/soda箱型) + 所有target = 4 的组合，就等于把所有组合都加上2，同理所有5的组合加上1，最终得到所有6的组合
                else:
                    for prevList in dp[t - sodas[j]]:
                        if sodas[j] >= prevList[-1]:
                            curr = prevList
                            curr.append(sodas[j])
                            tmp.append(curr)
                j += 1
            dp[t] = tmp
        return dp[N]