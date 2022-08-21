class Solution(object):
    def countAsterisks(self, s):
        res = 0
        flag = True
        for c in s:
            if flag is True and c == '*':
                res += 1
            elif flag is True and c == '|':
                flag = False
            elif flag is False and c == '|':
                flag = True
        return res