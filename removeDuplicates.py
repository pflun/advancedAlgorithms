class Solution(object):
    def removeDuplicates(self, nums):
        mem = set()
        if len(nums) == 0:
            return []
        for i in range(len(nums)):
            mem.add(nums[i])
        return list(mem)

    def removeDuplicates2(self, A):
        if not A:
            return 0

        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]

        return newTail + 1

test = Solution()
print test.removeDuplicates([1,1,2,3,3])