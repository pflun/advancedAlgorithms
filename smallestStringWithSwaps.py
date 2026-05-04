class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        self.dic = {i:i for i in range(len(s))}
        for p in pairs:
            self.union(p[0], p[1])
        # parent idx => [grouped chars] then sort grouped chars
        # {0: ['a', 'b', 'c', 'd']} or {0: ['b', 'd'], 1: ['a', 'c']}
        group = {}
        for i in range(len(s)):
            f = self.find(i)
            group[f] = group.get(f, []) + [s[i]]
        for comp_id in group.keys():
            group[comp_id].sort()
        res = []
        for i in range(len(s)):
            # for current idx, find parent idx then pop first char
            f = self.find(i)
            res.append(group[f].pop(0))
        return ''.join(res)

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

test = Solution()
print test.smallestStringWithSwaps("dcab", [[0,3],[1,2]])
print test.smallestStringWithSwaps("dcab", [[0,3],[1,2],[0,2]])
print test.smallestStringWithSwaps("cba", [[0,1],[1,2]])