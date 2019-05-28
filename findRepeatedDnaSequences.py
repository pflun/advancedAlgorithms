class Solution(object):
    def findRepeatedDnaSequences(self, s):
        r, record = set(), set()
        for i in xrange(len(s) - 9):
            substring = s[i:i + 10]
            if substring in record:
                r.add(substring)
            else:
                record.add(substring)
        return list(r)

test = Solution()
print test.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")