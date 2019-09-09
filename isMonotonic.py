# faster than do within one for loop
class Solution(object):
    def isMonotonic(self, A):
        increase = True
        decrease = True

        # increasing
        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                increase = False
                break

        # decreasing
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                decrease = False
                break

        return increase or decrease