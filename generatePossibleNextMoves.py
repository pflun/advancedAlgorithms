# -*- coding: utf-8 -*-
# You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend
# take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other
# person will be the winner.
# Write a function to compute all possible states of the string after one valid move.
class Solution:
    def generatePossibleNextMoves(self, s):
        if len(s) < 2:
            return []
        res = []

        for i in range(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                tmp = list(s)
                tmp[i], tmp[i + 1] = '-', '-'
                res.append(''.join(tmp))

        return res

test = Solution()
print test.generatePossibleNextMoves("++++")