# -*- coding: utf-8 -*-
# https://www.cnblogs.com/grandyang/p/6108158.html
# 不需要heap，直接dfs backtracking找所有解里面最小的
import heapq
class Solution(object):
    def minTransfers2(self, transactions):
        self.res = float('inf')
        dic = {}
        for t in transactions:
            x, y, z = t[0], t[1], t[2]
            dic[x] = dic.get(x, 0) - z
            dic[y] = dic.get(y, 0) + z
        accounts = []
        # filter out balance已经为0的
        for k, v in dic.items():
            if v != 0:
                accounts.append(v)
        self.helper(accounts, 0, 0)
        return self.res

    def helper(self, accounts, start, cnt):
        # pruning
        if cnt >= self.res:
            return
        # 跳过已经为0的
        while start < len(accounts):
            if accounts[start] == 0:
                start += 1
            else:
                break
        # 递归到结束
        if start == len(accounts):
            self.res = min(self.res, cnt)
            return
        # 如果下面某个跟当前符号不一样，抵消，dfs总能找到最小解
        # 把start变成0，递归start + 1 (子问题)
        for i in range(start + 1, len(accounts)):
            if (accounts[i] < 0 and accounts[start] > 0) or (accounts[i] > 0 and accounts[start] < 0):
                accounts[i] += accounts[start]
                self.helper(accounts, start + 1, cnt + 1)
                accounts[i] -= accounts[start]

    # 等等，这题貌似不是priority queue?
    def minTransfers(self, transactions):
        res = 0
        dic = {}
        for t in transactions:
            x, y, z = t[0], t[1], t[2]
            dic[x] = dic.get(x, 0) - z
            dic[y] = dic.get(y, 0) + z
        positive = []
        negative = []
        heapq.heapify(positive)
        heapq.heapify(negative)
        for v in dic.values():
            if v > 0:
                heapq.heappush(positive, -v)
            elif v < 0:
                heapq.heappush(negative, v)
        while positive and negative:
            currP = -heapq.heappop(positive)
            currN = heapq.heappop(negative)
            remain = currP + currN
            if remain > 0:
                heapq.heappush(positive, -remain)
            elif remain < 0:
                heapq.heappush(negative, remain)
            res += 1
        return res

test = Solution()
print test.minTransfers2([[0,1,10], [1,0,1], [1,2,5], [2,0,5]])
print test.minTransfers2([[0,1,10], [2,0,5]])
print test.minTransfers2([[1, 8, 1], [1, 9, 1], [2, 8, 10], [3, 9, 20], [4, 10, 30], [5, 11, 40], [6, 12, 50], [7, 13, 60], [20, 80, 10], [30, 90, 20], [40, 100, 30], [50, 110, 40], [60, 120, 50], [70, 130, 60]])