# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=GRRDl3HxQAI
class Solution(object):
    def minimumDistance(self, word):
        # kRest代表悬空
        kRest = 26
        mem = [[[None for _ in range(27)] for _ in range(27)] for _ in range(len(word))]

        def cost(c1, c2):
            if c1 == kRest:
                return 0
            return abs(c1 / 6 - c2 / 6) + abs(c1 % 6 - c2 % 6)

        # min cost to type/complete word[i:], 左右手分别在 l, r 这两个index上
        def dp(i, l, r):
            # 打印完了
            if i == len(word):
                return 0
            if mem[i][l][r]:
                return mem[i][l][r]
            # 相对index
            c = ord(word[i]) - ord('A')
            # min( 左手挪到 c 后的状态 + cost(l, c), 右手同理 )
            mem[i][l][r] = min(dp(i + 1, c, r) + cost(l, c), dp(i + 1, l, c) + cost(r, c))
            return mem[i][l][r]

        return dp(0, kRest, kRest)

test = Solution()
print test.minimumDistance('CAKE')
print test.minimumDistance('HAPPY')