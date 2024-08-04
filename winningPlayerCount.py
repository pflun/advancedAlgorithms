class Solution(object):
    def winningPlayerCount(self, n, pick):
        res = 0
        dic = {}
        for p in pick:
            player = p[0]
            color = p[1]
            if player in dic:
                dic[player][color] = dic[player].get(color, 0) + 1
            else:
                dic[player] = {color: 1}
        for k, v in dic.items():
            max_ball = 0
            for b in v.values():
                max_ball = max(max_ball, b)
            if max_ball > k:
                res += 1
        return res

test = Solution()
print test.winningPlayerCount(2, [[1,3],[1,3],[0,10],[1,6]])