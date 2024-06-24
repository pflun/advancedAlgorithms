class Solution(object):
    def numberOfChild(self, n, k):
        # no matter how many travels, find out the last direction
        dir = k / (n - 1)
        # position at last travel
        reminder = k % (n - 1)
        # last travel from left to right
        if dir % 2 == 0:
            return reminder
        # last travel from right to left
        else:
            return n - reminder - 1
