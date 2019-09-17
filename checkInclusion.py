class Solution(object):
    def checkInclusion(self, s1, s2):
        dic1 = {}
        dic2 = {}
        for s in s1:
            dic1[s] = dic1.get(s, 0) + 1
        for i in range(len(s1)):
            dic2[s2[i]] = dic2.get(s2[i], 0) + 1
        if self.equals(dic1, dic2):
            return True
        for i in range(len(s2) - len(s1)):
            # remove left end
            rm = s2[i]
            # add right end
            ad = s2[i + len(s1)]
            dic2[rm] -= 1
            if dic2[rm] == 0:
                dic2.pop(rm)
            dic2[ad] = dic2.get(ad, 0) + 1
            if self.equals(dic1, dic2):
                return True
        return False

    def equals(self, dic1, dic2):
        return True if dic1 == dic2 else False

test = Solution()
print test.checkInclusion("ab", "eidbaooo")
print test.checkInclusion("ab", "eidoaoba")
print test.checkInclusion("ab", "eidboaoo")