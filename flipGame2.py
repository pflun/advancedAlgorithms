# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=x2CpdxyviLA
# memory = {'string' => '能/不能赢'}
#
class Solution:
    def canWin(self, s):
        if not s or len(s) == 0:
            return False
        memory = {}

        return self.backtracking(s, memory)

    def backtracking(self, s, memory):
        # 在mem里直接return结果
        if s in memory:
            return memory[s]
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                opponent = s[:i] + '--' + s[i + 2:]
                # 如果对手False，自己就返回True
                if not self.backtracking(opponent, memory):
                    memory[s] = True
                    return True

        # 一直都没有赢，就return False输
        memory[s] = False
        return False

test = Solution()
print test.canWin("++++")