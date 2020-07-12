class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        if target > m:
            return -1
        cache = [[[float('inf') for _ in range(n + 1)] for _ in range(m)] for _ in range(m)]
        for i in range(1, m - target + 2):
            for j in range(m - i + 1):
                for k in range(1, n + 1):
                    isPass = True
                    idx = j
                    cur = 0
                    while isPass and idx < j + i:
                        if houses[idx] == k:
                            idx += 1
                            continue
                        elif houses[idx] != 0:
                            isPass = False
                        else:
                            cur += cost[idx][k - 1]
                        idx += 1
                    if isPass:
                        cache[j][j + i - 1][k] = cur
        res = self.dfs({}, cache, -1, 0, target, m, n, m)
        if res == float('inf'):
            return -1
        else:
            return res

    def dfs(self, map, cache, preGroup, curIndex, remainteam, m, n, size):
        if curIndex >= m:
            if remainteam == 0:
                return 0
            else:
                return float('inf')
        if remainteam == 0:
            return float('inf')
        key = curIndex + ',' + preGroup + ',' + remainteam
        if key in map:
            return map[key]
        minNum = float('inf')
        for j in range(1, n + 1):
            if j == preGroup:
                continue
            i = 1
            while i <= size and curIndex + i <= m:
                mid = cache[curIndex][curIndex + i - 1][j]
                if mid == float('inf'):
                    break
                remain = dfs(map, cache, j, curIndex + i, remainteam - 1, m, n, size - i)
                if remainteam == float('inf'):
                    continue
                minNum = min(minNum, mid + remain)
                i += 1
        map[key] = minNum
        return minNum