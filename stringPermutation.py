class Solution:
    # @param {string} A a string
    # @param {string} B a string
    # @return {boolean} a boolean
    def stringPermutation(self, A, B):
        dicA = {}
        dicB = {}

        for i in A:
            dicA[i] = dicA.get(i, 0) + 1
        for j in B:
            dicB[j] = dicB.get(j, 0) + 1

        return dicA == dicB

test = Solution()
print test.stringPermutation("abc", "bca")