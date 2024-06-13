class Solution(object):
    def maximumCostSubstring(self, s, chars, vals):
        dic = {}
        for i in range(len(chars)):
            dic[chars[i]] = vals[i]
        dp = [0]
        for i in range(len(s)):
            currStr = s[i]
            if currStr in dic:
                currVal = dic[currStr]
            else:
                currVal = ord(currStr) - 96
            dp.append(max(0, dp[-1] + currVal))
        return max(dp)

test = Solution()
print test.maximumCostSubstring("adaa", "d", [-1000])
print test.maximumCostSubstring("abc", "abc", [-1,-1,-1])
print test.maximumCostSubstring("talaqlt", "tqla", [4,3,3,-2])