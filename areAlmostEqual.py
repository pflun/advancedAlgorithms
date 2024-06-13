class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        dic1 = {}
        dic2 = {}
        for c in s1:
            dic1[c] = dic1.get(c, 0) + 1
        for c in s2:
            dic2[c] = dic2.get(c, 0) + 1
        if dic1 != dic2:
            return False
        i = 0
        cnt = 0
        while i < len(s1):
            if s1[i] != s2[i]:
                cnt += 1
                if cnt > 2:
                    return False
            i += 1
        return True if cnt == 0 or cnt == 2 else False

    def areAlmostEqual2(self, s1, s2):
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        i = 0
        cnt = 0
        while i < len(s1):
            if s1[i] != s2[i]:
                cnt += 1
                if cnt > 2:
                    return False
            i += 1
        return True

test = Solution()
print test.areAlmostEqual("bank", "kanb")
print test.areAlmostEqual("attack", "defend")
print test.areAlmostEqual("kelb", "kelb")
print test.areAlmostEqual("abcd", "dcba")
print test.areAlmostEqual2("bank", "kanb")
print test.areAlmostEqual2("abcd", "dcba")