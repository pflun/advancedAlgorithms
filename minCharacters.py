class Solution(object):
    def minCharacters2(self, a, b):
        def find(a, b):
            res = float('inf')
            aa = [0 for _ in range(26)]
            bb = [0 for _ in range(26)]
            for i in a:
                aa[ord(i) - ord('a')] += 1
            for i in b:
                bb[ord(i) - ord('a')] += 1
            for i in range(1, 26):
                cur = 0
                for j in range(i):
                    cur += bb[j]
                for j in range(i, 26):
                    cur += aa[j]
                res = min(res, cur)
            return res

        def freq(a):
            aa = [0] * 26
            for i in a:
                aa[ord(i) - ord('a')] += 1
            return max(aa)

        return min(find(a, b), find(b, a), len(a) + len(b) - freq(a) - freq(b))

    # minor corner case not pass
    def minCharacters(self, a, b):
        res = float('inf')
        freqA = [0 for _ in range(26)]
        freqB = [0 for _ in range(26)]
        for c in a:
            freqA[ord(c) - 97] = freqA[ord(c) - 97] + 1
        for c in b:
            freqB[ord(c) - 97] = freqB[ord(c) - 97] + 1

        for i in range(1, 26):
            costA = sum(freqA[i:])
            costB = sum(freqB[:i])
            res = min(res, costA + costB)
        for i in range(25):
            costA = sum(freqA[:i])
            costB = sum(freqB[i:])
            res = min(res, costA + costB)
        # Solution 3
        res = min(res, len(a) + len(b) - max(freqA) - max(freqB))
        return res

test = Solution()
print test.minCharacters("aba", "caa")
print test.minCharacters("dabadd", "cda")
print test.minCharacters("e", "e")