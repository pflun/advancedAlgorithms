class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        length = length + string.count(' ') * 2
        string = string.replace(" ", "%20")
        return string

test = Solution()
print test.replaceBlank("hello world", 11)

# https://www.kancloud.cn/kancloud/data-structure-and-algorithm-notes/72942