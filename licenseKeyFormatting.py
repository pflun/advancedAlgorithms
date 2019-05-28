class Solution(object):
    def licenseKeyFormatting(self, S, K):
        res = []
        S = ''.join(S.split("-"))

        ct = 0
        tmp = ''
        for i in range(len(S) - 1, -1, -1):
            if ct == K:
                res.append(tmp[::-1])
                tmp = S[i].upper()
                ct = 0
            else:
                tmp += S[i].upper()
                ct += 1

        if len(tmp) != 0:
            res.append(tmp[::-1])

        return '-'.join(res[::-1])

test1 = Solution()
print test1.licenseKeyFormatting("5F3Z-2e-9-w", 4)