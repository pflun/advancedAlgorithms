class Solution(object):
    def compressedString(self, word):
        res = ''
        cnt = 0
        curr = ''
        for w in word:
            if cnt == 0:
                cnt = 1
                curr = w
                continue
            if w == curr:
                cnt += 1
                if cnt == 9:
                    res += '9' + curr
                    cnt = 0
                    curr = ''
            else:
                res += str(cnt) + curr
                cnt = 1
                curr = w
        if cnt != 0:
            res += str(cnt) + curr
        return res

test = Solution()
print test.compressedString("abcde")
print test.compressedString("aaaaaaaaaaaaaabb")
# "8y3f4c2q2w8f9r5a9y"
print test.compressedString("yyyyyyyyfffccccqqwwffffffffrrrrrrrrraaaaayyyyyyyyy")