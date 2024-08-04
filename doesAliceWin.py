class Solution(object):
    # number of vowels is 0, bob win, alice cannot take any
    # number of vowels is odd, alice take all and win
    # number of vowels is even, alice win because firstly she'll take odd number, then bob take even number (0), then alice take odd
    def doesAliceWin(self, s):
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        cnt = 0
        for c in s:
            if c in vowels:
                cnt += 1
        return False if cnt == 0 else True