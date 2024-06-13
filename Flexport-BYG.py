# -*- coding: utf-8 -*-
# 给两个String，一个是target一个是guess，然后根据每个字母在两个字符串里面的位置返回一个string， 用B(black)/Y(yellow)/G(green) 表示。如果guess里面某一个字母在target里没有的话就是B, 有但是位置不同就是Y，有而且位置相同就是G. 比如 target = "SMILE", guess = "CLOSE" 返回 "BYBYG".
# 第一问：假设target里面没有重复的字母.
# 第二问：假设target里面有重复的字母，用过就不能再用，优先配对位置相同的。比如 target = "BBAAA", guess = "CCCAA" 返回的就是BBBGG （优先配对后两个位置相同的A）
# 第三问：加了一点ood，就说如果是个游戏，然后每一轮有maxattempt，怎么设计+改之前写好的method
class Solution(object):
    # no repeat
    def guessWord(self, target, guess):
        dic = {}
        for i in range(len(target)):
            dic[target[i]] = i
        res = ''
        for i in range(len(guess)):
            if guess[i] in dic and i == dic[guess[i]]:
                res += 'G'
            elif guess[i] in dic:
                res += 'Y'
            else:
                res += 'B'
        return res

    # with repeat
    def guessWord2(self, target, guess):
        res = [None for _ in range(len(guess))]
        used = set()
        for i in range(len(target)):
            if target[i] == guess[i]:
                res[i] = 'G'
                used.add(i)
        dic = {}
        for i in range(len(target)):
            if i in used:
                continue
            if target[i] not in dic:
                dic[target[i]] = set()
            dic[target[i]].add(i)
        for i in range(len(guess)):
            if i in used:
                continue
            if guess[i] in dic and i in dic[guess[i]]:
                res[i] = 'Y'
                dic[guess[i]].remove(i)
            else:
                res[i] = 'B'
        return "".join(res)

test = Solution()
print test.guessWord("SMILE", "CLOSE")
print test.guessWord2("BBAAA", "CCCAA")