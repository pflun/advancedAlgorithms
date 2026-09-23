# -*- coding: utf-8 -*-
# 假设把所有人运到A city，再按照谁从A换到B能省更多钱，把一半人换到B city
class Solution(object):
    def twoCitySchedCost(self, costs):
        refund = []
        # 把人从A换到B的cost
        for c in costs:
            refund.append(c[1] - c[0])
        # 负得越多，省的越多
        refund.sort()
        res = 0
        # move all to city A
        for c in costs:
            res += c[0]
        for i in range(len(costs) / 2):
            res += refund[i]
        return res

    # dp[i][j] represents the cost when considering first (i + j) people in which i people assigned to city A and j people assigned to city B.
    def twoCitySchedCost2(self, costs):
        n = len(costs) / 2  # n people go to A, n people go to B
        # dp[i][j] = min cost when i people sent to A, j people sent to B
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Base: send first i people all to city A
        for i in range(1, n + 1):
            dp[i][0] = dp[i-1][0] + costs[i-1][0]

        # Base: send first j people all to city B
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] + costs[j-1][1]

        # Fill: person at index (i+j-1) goes to A or B, take min
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                person = i + j - 1   # 0-indexed into costs
                dp[i][j] = min(
                    dp[i-1][j] + costs[person][0],  # send to A
                    dp[i][j-1] + costs[person][1]   # send to B
                )

        return dp[n][n]

    # Quick Select Solution (Average O(N) Time, O(1) Space)
    # 思想：我们不需要完全排序，只需要把 a-b 差值最小的 n 个人丢到数组左半边即可
    def twoCitySchedCost3(self, costs):
        n = len(costs) / 2

        def get_diff(c):
            return c[0] - c[1]

        def quick_select(left, right, k):
            if left >= right: return

            # 1. 选最右边作为基准 (pivot)
            pivot_val = get_diff(costs[right])
            p = left

            # 2. 把所有小于等于 pivot 的元素丢到 p 的左边
            for i in range(left, right):
                if get_diff(costs[i]) <= pivot_val:
                    costs[p], costs[i] = costs[i], costs[p]
                    p += 1
            # 把 pivot 放到它应该在的 p 的位置
            costs[p], costs[right] = costs[right], costs[p]

            # 3. 判断 p 是不是我们要找的分界线 k
            if p == k:
                return
            elif p < k:
                quick_select(p + 1, right, k)
            else:
                quick_select(left, p - 1, k)

        # 找索引为 n 的位置，它会自动把最小的 n 个元素（0 到 n-1）丢到左半边
        quick_select(0, len(costs) - 1, n)

        res = 0
        # 左半边（0 到 n-1）全去 A
        for i in range(n):
            res += costs[i][0]
        # 右半边（n 到 2n-1）全去 B
        for i in range(n, len(costs)):
            res += costs[i][1]

        return res

test = Solution()
print test.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])
print test.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])
print test.twoCitySchedCost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]])