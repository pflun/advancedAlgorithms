class Solution(object):
    def minSwap(self, S):
        res = 0
        i = 0
        while i < len(S):
            j = i + 1
            while j < len(S) and S[j] == S[i]:
                j += 1
            tmp = j - i
            if tmp >= 3:
                res += (j - i) / 3
            i = j
        return res

test = Solution()
print test.minSwap('baaaaa')
print test.minSwap('baaabbaabbba')
print test.minSwap('baabab')
print test.minSwap('')
print test.minSwap('bb')
print test.minSwap('bbb')