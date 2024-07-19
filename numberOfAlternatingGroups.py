class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        colors = colors[-2:] + colors
        res = 0
        for i in range(len(colors) - 2):
            if colors[i] != colors[i + 1] and colors[i + 1] != colors[i + 2]:
                res += 1
        return res

test = Solution()
print test.numberOfAlternatingGroups([1,1,1])
print test.numberOfAlternatingGroups([0,1,0,0,1])