class Solution(object):
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False
        elif A is None and B is None:
            return True

        res = []
        for i in range(len(A)):
            if A[i] != B[i]:
                res.append(i)

        if len(res) == 2 and A[res[0]] == B[res[1]] and A[res[1]] == B[res[0]]:
            return True
        elif len(res) == 0 and len(set(A)) == 1:
            return True
        else:
            return False

test = Solution()
print test.buddyStrings("aaaaaaa", "aaaaaaa")