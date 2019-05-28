class Solution(object):
    def maxRotateFunction(self, A):
        self.res = 0

        def helper(A):
            res = 0
            m = 0
            for a in A:
                res += a * m
                m += 1

            return res

        for offset in range(len(A)):
            if offset == 0:
                tmp = A
            else:
                tmp = A[len(A) - offset:] + A[:-offset]

            self.res = max(self.res, helper(tmp))

        return self.res

test = Solution()
print test.maxRotateFunction([4, 3, 2, 6])