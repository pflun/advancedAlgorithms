class Solution(object):
    def backspaceCompare(self, S, T):
        def backspace(chars):
            res = ''
            for i in range(len(chars)):
                if chars[i] == '#':
                    if res == '':
                        continue
                    res = res[:-1]
                else:
                    res += chars[i]
            return res

        return backspace(S) == backspace(T)

    # O(1)
    # If we do it backward, we meet a char and we can be sure this char won't be deleted.
    # If we meet a '#', it tell us we need to skip next lowercase char.
    # The idea is that, read next letter from end to start.
    # If we meet #, we increase the number we need to step back, until back = 0
    def backspaceCompareO1(self, S, T):
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0
        while True:
            while i >= 0 and (backS or S[i] == '#'):
                backS += 1 if S[i] == '#' else -1
                i -= 1
            while j >= 0 and (backT or T[j] == '#'):
                backT += 1 if T[j] == '#' else -1
                j -= 1
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1
            i, j = i - 1, j - 1

test = Solution()
print test.backspaceCompare("ab##", "c#d#")
print test.backspaceCompare("y#fo##f", "y#f#o##f")