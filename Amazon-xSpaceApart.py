# -*- coding: utf-8 -*-
# given n pairs of numbers (1122...nn) and arrange them so that the each number x is x spaces apart from another number x.
# (数字必须紧挨着，思路就是DFS)


class Solution(object):
    def xSpaceApart(self, string):
        if len(string) % 2 != 0:
            return False

        self.res = ''

        def dfs(string, index):
            if index >= len(string):
                return

            self.res += string[index]

            for _ in range(int(string[index])):
                self.res += ' '

            self.res += string[index + 1]

            dfs(string, index + 2)

        dfs(string, 0)

        return self.res


test = Solution()
print test.xSpaceApart('1122335577')