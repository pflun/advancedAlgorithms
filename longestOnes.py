# https://www.youtube.com/watch?v=g1eMPnclJfU
class Solution(object):
    def longestOnes(self, A, K):
        left = 0
        right = 0
        # how many 0 has used
        zeros = 0
        res = 0
        while right < len(A):
            if A[right] == 0:
                zeros += 1
            # move left pointer
            while zeros > K:
                if A[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res

test = Solution()
print test.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)