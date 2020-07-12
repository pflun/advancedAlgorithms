class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        visited = set()
        self.dic = {}
        for i in range(len(favoriteCompanies)):
            self.dic[i] = i

        for i in range(len(favoriteCompanies)):
            for j in range(len(favoriteCompanies)):
                if i != j and j not in visited and self.isSubset(favoriteCompanies[j], favoriteCompanies[i]):
                    visited.add(j)
                    self.union(i, j)
        res = []
        for k, v in self.dic.items():
            if k == v:
                res.append(v)
        return res

    def find(self, x):
        parent = self.dic[x]
        while parent != self.dic[parent]:
            parent = self.dic[parent]
        return parent

    def union(self, master, branch):
        fa_master = self.find(master)
        fa_branch = self.find(branch)
        if fa_master != fa_branch:
            self.dic[fa_branch] = fa_master

    def isSubset(self, f2, f1):
        hashSet = set(f1)
        for f in f2:
            if f not in hashSet:
                return False
        return True

test = Solution()
# print test.isSubset(["google","facebook"], ["leetcode","google","facebook"])
# print test.isSubset(["leetcode","google","facebook"], ["google","microsoft"])
print test.peopleIndexes([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]])
print test.peopleIndexes([["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]])
print test.peopleIndexes([["leetcode"],["google"],["facebook"],["amazon"]])