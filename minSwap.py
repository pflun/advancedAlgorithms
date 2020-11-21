class Solution(object):
    def minSwap(self, A, B):
        swap = [1] + [len(A) for _ in range(len(A) - 1)]
        unswap = [0] + [len(A) for _ in range(len(A) - 1)]
        for i in range(1, len(A)):
            # need to swap both i and i - 1 to ensure increasing (or not swap at both)
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                swap[i] = swap[i - 1] + 1
                unswap[i] = unswap[i - 1]
            # only swap i or only swap i - 1 can ensure increasing
            elif A[i] > B[i - 1] and B[i] > A[i - 1]:
                swap[i] = min(unswap[i - 1] + 1, swap[i])
                unswap[i] = min(swap[i - 1], unswap[i])
        return min(swap[-1], unswap[-1])

test = Solution()
print test.minSwap([1,3,5,4], [1,2,3,7])