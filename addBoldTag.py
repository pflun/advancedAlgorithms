class Solution(object):
    def addBoldTag(self, s, dict):
        intervals = []
        merged = []
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i:j] in dict:
                    intervals.append([i, j])
        # merge interval
        for interval in intervals:
            if len(merged) == 0 or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        offsetIdx = 0
        for m in merged:
            startIdx = m[0] + offsetIdx
            s = s[:startIdx] + '<b>' + s[startIdx:]
            offsetIdx += 3
            endIdx = m[1] + offsetIdx
            s = s[:endIdx] + '</b>' + s[endIdx:]
            offsetIdx += 4

        return s

test = Solution()
dict = set(["aaa","aab","bc"])
print test.addBoldTag("aaabbcc", dict)