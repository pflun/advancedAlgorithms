# -*- coding: utf-8 -*-
# https://leetcode.com/problems/repeated-dna-sequences/discuss/53902/Short-Java-%22rolling-hash%22-solution
# rolling-hash算法就是rolling过程中，每次把整个hash ^ 4，因为10 letters最左边每次减掉 4 ^ 9 * 最左边的值，因为最左边一位rolling到该减去的时候恰好是幂了9次（4 ^ 9 * 最左边的值）
import math
class Solution(object):
    # rolling-hash
    def findRepeatedDnaSequences2(self, s):
        dic = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        A_SIZE_POW_9 = math.pow(len(dic), 9)
        res = set()
        visited = set()
        rhash = 0
        for i in range(len(s)):
            if i > 9:
                rhash -= A_SIZE_POW_9 * dic[s[i - 10]]
            rhash = len(dic) * rhash + dic[s[i]]
            # == 9 cover corner case that first 10-letter shaped, AAAAACCCCC
            if i >= 9:
                if rhash in visited:
                    res.add(s[i - 9: i + 1])
                visited.add(rhash)
        return list(res)

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
print test.findRepeatedDnaSequences2("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")