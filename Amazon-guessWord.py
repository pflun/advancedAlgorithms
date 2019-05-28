# -*- coding: utf-8 -*-
# 设计一个猜单词API，不用考虑ui display，user每次猜一个char如果猜对了就把对应位置的字符显示出来，
# user如果累计猜错7次就宣布游戏结束，这个感觉很偏OOD，没什么算法可言，hashmap就能搞定
class Solution(object):
    def __init__(self, word):
        self.word = word
        self.curr = '*' * len(word)
        self.dic = {}
        self.life = 7

        for w in word:
            self.dic[w] = self.dic.get(w, 0) + 1

    def guessWord(self, char):
        if len(char) != 1:
            self.life -= 1
            if self.life == 0:
                print 'Game Over'
            return False

        if char in self.dic:
            self.dic[char] -= 1
            if self.dic[char] == 0:
                self.dic.pop(char)
            pw = 0
            while pw < len(self.word):
                if self.word[pw] == char and self.curr[pw] == '*':
                    tmp = list(self.curr)
                    tmp[pw] = char
                    self.curr = ''.join(tmp)
                pw += 1
        else:
            self.life -= 1
            if self.life == 0:
                print 'Game Over'
            return False

        return self.curr

test = Solution('word')
print test.guessWord('w')
print test.guessWord('r')
print test.guessWord('a')