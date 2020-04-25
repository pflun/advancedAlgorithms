class Solution(object):
    def __init__(self):
        self.relationship = []
        self.dic = {}

    def numSimilarGroups(self, A):
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                if self.isSimilar(A[i], A[j]):
                    self.relationship.append([i, j])

        # init UF
        for a in A:
            self.dic[a] = a

        for r in self.relationship:
            self.union(A[r[0]], A[r[1]])

        res = 0
        for k, v in self.dic.items():
            if k == v:
                res += 1
        return res

    def find(self, x):
        while x != self.dic[x]:
            x = self.dic[x]
        return x

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.dic[px] = py

    def isSimilar(self, a, b):
        cnt = 0
        i = 0
        while i < len(a):
            if a[i] != b[i]:
                cnt += 1
            i += 1
        return True if cnt == 0 or cnt == 2 else False

test = Solution()
print test.numSimilarGroups(["tars","rats","arts","star"])
# print test.isSimilar("tars", "rats")