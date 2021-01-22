class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        res = 0
        used = set()
        self.dic = {}
        self.map = {}
        for a in allowedSwaps:
            if a[0] not in self.dic:
                self.dic[a[0]] = a[0]
            if a[1] not in self.dic:
                self.dic[a[1]] = a[1]
            self.union(a[0], a[1])
        for a in allowedSwaps:
            fa = self.find(a[0])
            if fa in self.map:
                self.map[fa].add(a[0])
                self.map[fa].add(a[1])
            else:
                self.map[fa] = set([a[0], a[1]])
        for k, v in self.map.items():
            tmp1 = []
            tmp2 = []
            for i in v:
                tmp1.append(source[i])
                tmp2.append(target[i])
                used.add(i)
            tmp1.sort()
            tmp2.sort()
            i = 0
            j = 0
            cnt = 0
            while i < len(tmp1) and j < len(tmp2):
                if tmp1[i] < tmp2[j]:
                    i += 1
                elif tmp1[i] > tmp2[j]:
                    j += 1
                else:
                    cnt += 1
                    i += 1
                    j += 1
            res += len(tmp1) - cnt
        for i in range(len(source)):
            if i not in used:
                if source[i] != target[i]:
                    res += 1
        return res

    def find(self, x):
        if x != self.dic[x]:
            self.dic[x] = self.find(self.dic[x])
        return self.dic[x]

    def union(self, master, branch):
        fa_master = self.find(master)
        fa_branch = self.find(branch)
        if fa_master != fa_branch:
            self.dic[fa_branch] = fa_master

test = Solution()
print test.minimumHammingDistance([1,2,3,4], [2,1,4,5], [[0,1],[2,3]])
print test.minimumHammingDistance([1,2,3,4], [1,3,2,4], [])
print test.minimumHammingDistance([5,1,2,4,3], [1,5,4,2,3], [[0,4],[4,2],[1,3],[1,4]])
print test.minimumHammingDistance([85,91], [77,50], [[1,0]])