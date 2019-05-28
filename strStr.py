class Solution:
    """
    @param: : source string to be scanned.
    @param: : target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """

    def strStr(self, source, target):
        if target == '':
            return 0
        if target in source:
            return len(source.split(target)[0])
        return -1


class Solution1:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        for i in range(len(needle), len(haystack) + 1):
            if haystack[i - len(needle):i] == needle:
                return i - len(needle)

        return -1

class Solution2:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            # if the slice from i til i + len(needle) is exact needle
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

test = Solution2()
print test.strStr("abcdabcdefg", "cdefg")