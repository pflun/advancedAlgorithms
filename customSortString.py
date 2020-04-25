class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        if len(T) == 0:
            return ''
        elif len(T) == 1:
            return T
        elif len(T) == 2:
            c1 = T[0]
            c2 = T[1]
            if self.comparator(c1, c2, S):
                return T
            else:
                return c2 + c1
        pivot = T[0]
        small = ''
        large = ''
        for c in T[1:]:
            if self.comparator(c, pivot, S):
                small += c
            else:
                large += c
        left = self.customSortString(S, small)
        right = self.customSortString(S, large)
        return left + pivot + right

    def comparator(self, a, b, S):
        if S.find(a) > S.find(b):
            return False
        else:
            return True

test = Solution()
print test.customSortString("cba", "abcd")