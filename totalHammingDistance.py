class Solution(object):
    def totalHammingDistance(self, nums):
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                res += self.getHammingDiff(bin(nums[i])[2:], bin(nums[j])[2:])
        return res

    def getHammingDiff(self, A, B):
        i = 0
        cnt = 0
        A = A[::-1]
        B = B[::-1]
        while i < len(A) and i < len(B):
            if A[i] != B[i]:
                cnt += 1
            i += 1
        return cnt + abs(len(A) - len(B))

test = Solution()
print test.getHammingDiff('0100', '1110')
print test.totalHammingDistance([4, 14, 2])