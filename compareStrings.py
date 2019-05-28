class Solution:
    def compareStrings(self, A, B):
        dic = {}
        for i in A:
            dic[i] = dic.get(i, 0) + 1
        for i in B:
            dic[i] = dic.get(i, 0) - 1
        for key, val in dic.items():
            if val < 0:
                return False
        return True


test = Solution()
print test.compareStrings("ABCD", "AACDF")