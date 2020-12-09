import string
class Solution(object):
    def getSmallestString2(self, n, k):
        dic = {ord(x) - 96: x for x in string.ascii_lowercase}
        z_cnt = 0
        res = []
        remain = k - n
        while remain >= 25:
            remain -= 25
            z_cnt += 1
        isMid = 1 if remain > 0 else 0
        for _ in range(n - z_cnt - isMid):
            res.append('a')
        if isMid:
            mid = dic[remain + 1]
            res.append(mid)
        for _ in range(z_cnt):
            res.append('z')
        return ''.join(res)

    def getSmallestString(self, n, k):
        dic = { ord(x) - 96 : x for x in string.ascii_lowercase }
        res = []
        for _ in range(n):
            res.append('a')
        remain = k - n
        offset = n - 1
        while remain > 0:
            if remain >= 25:
                res = res[:offset] + ['z'] + res[offset + 1:]
                offset -= 1
                remain -= 25
            else:
                curr = dic[remain + 1]
                res = res[:offset] + [curr] + res[offset + 1:]
                offset -= 1
                remain = 0
        return ''.join(res)


test = Solution()
print test.getSmallestString2(5, 73)
print test.getSmallestString2(3, 27)
# print test.getSmallestString2(29795, 746845)