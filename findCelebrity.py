# -*- coding: utf-8 -*-
class Solution:
    def findCelebrity(self, n):
        if n < 2:
            return False
        possible = 0
        # 这个循环会导致possible卡在名人这点，前面都认识名人i，名人i不认识后面的人（所以卡在i）
        for i in range(1, n):
            if self.knows(possible, i):
                possible = i

        # 验证
        for j in range(n):
            # 不是possible自己 and 名人认识某个人 或 有人不认识名人
            if j != possible and (self.knows(possible, i) or not self.knows(i, possible)):
                return False

        return possible

    # 防报错
    def knows(self, a, b):
        return True