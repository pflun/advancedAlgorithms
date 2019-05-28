class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        s = s.split()
        print s
        if len(s) == 0:
            return 0
        return len(s[-1])

test = Solution()
print test.lengthOfLastWord("b a ")