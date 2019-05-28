class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''

        minSize = float('inf')
        # get min str length
        for str in strs:
            minSize = min(minSize, len(str))

        # compare strs from first position
        for i in range(minSize):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[j - 1][i]:
                    return strs[j][:i]
        return strs[0][:minSize]

test = Solution()
# print test.longestCommonPrefix(['tree', 'trie', 'trill'])
print test.longestCommonPrefix(["aa","a"])