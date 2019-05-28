class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        longest = []
        counter = 0
        for key, val in dictionary.items():
            if len(val) > counter:
                del longest[:]
                longest.append(val)
                counter = len(val)
            elif len(val) == counter:
                longest.append(val)
        return longest

test = Solution()
print test.longestWords({"like","love","hate","yes"})