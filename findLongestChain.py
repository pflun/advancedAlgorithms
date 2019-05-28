class Solution(object):
    def findLongestChain(self, pairs):
        res = 0
        curr = -float('inf')
        end = sorted(pairs, key=lambda x: x[1])

        for e in end:
            if curr < e[0]:
                res += 1
                curr = e[1]

        return res

test = Solution()
print test.findLongestChain([[1,2], [2,3], [3,4]])