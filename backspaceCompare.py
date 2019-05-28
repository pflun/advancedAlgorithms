class Solution(object):
    def backspaceCompare(self, S, T):
        resS = ""
        resT = ""

        for i in range(len(S)):
            if S[i] == "#" and len(resS) > 0:
                resS = resS[:-1]
            else:
                resS += S[i]

        for i in range(len(T)):
            if T[i] == "#" and len(resT) > 0:
                resT = resT[:-1]
            else:
                resT += T[i]

        return True if resS == resT else False

test = Solution()
print test.backspaceCompare("ab##", "c#d#")