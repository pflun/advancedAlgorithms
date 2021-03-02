# simply do: res += n * (n + 1) / 2 would calculate total = 1 + 2 + ... + n
class Solution(object):
    def countHomogenous(self, s):
        res = 0
        cnt = 1
        for i in range(len(s)):
            if i == len(s) - 1:
                if s[i] == s[i - 1]:
                    tmp = 0
                    for j in range(1, cnt + 1):
                        tmp += j
                    res += tmp
                else:
                    res += 1
                break
            if s[i] == s[i + 1]:
                cnt += 1
                continue
            else:
                if cnt == 1:
                    res += 1
                else:
                    tmp = 0
                    for j in range(1, cnt + 1):
                        tmp += j
                    res += tmp
                cnt = 1

        return res % (10 ** 9 + 7)

test = Solution()
print test.countHomogenous("abbcccaa")
print test.countHomogenous("xy")
print test.countHomogenous("zzzzz")