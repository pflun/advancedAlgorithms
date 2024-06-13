# -*- coding: utf-8 -*-
# 一个点被pushed or not，取决于距离它最近的L和R
class Solution(object):
    def pushDominoes(self, dominoes):
        res = list(dominoes)
        for i in range(len(res)):
            if res[i] == '.':
                distanceR = float('inf')
                distanceL = float('inf')
                # find R from left
                for j in range(i - 1, -1, -1):
                    # 在左侧找R但先遇到L，意味着传导不到i点
                    if res[j] == 'L':
                        break
                    if res[j] == 'R':
                        distanceR = abs(i - j)
                        break
                # find L from right
                for j in range(i + 1, len(res)):
                    if res[j] == 'R':
                        break
                    if res[j] == 'L':
                        distanceL = abs(j - i)
                        break
                if distanceL == distanceR:
                    continue
                # 先替换成小写不影响后续查找LR
                elif distanceR < distanceL:
                    res[i] = 'r'
                elif distanceR > distanceL:
                    res[i] = 'l'
        return ''.join(res).replace("r", "R").replace("l", "L")

test = Solution()
print test.pushDominoes("RR.L")
print test.pushDominoes(".L.R...LR..L..")
