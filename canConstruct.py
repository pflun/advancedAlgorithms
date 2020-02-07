class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
        dic1 = {}
        dic2 = {}
        for c in magazine:
            dic1[c] = dic1.get(c, 0) + 1
        for c in ransomNote:
            dic2[c] = dic2.get(c, 0) + 1
        for k, v in dic2.items():
            if k not in dic1:
                return False
            else:
                if v > dic1[k]:
                    return False
        return True