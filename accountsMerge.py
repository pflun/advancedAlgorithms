class Solution(object):
    def accountsMerge(self, accounts):
        self.res = []
        self.dic = {}
        self.visited = set()
        # build reverse idx, johnsmith@mail.com => [0, 2]
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in self.dic:
                    self.dic[accounts[i][j]].append(i)
                else:
                    self.dic[accounts[i][j]] = [i]

        def dfs(i, accounts, tmp):
            if i in self.visited:
                return
            self.visited.add(i)
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                tmp.add(email)
                for idx in self.dic[email]:
                    dfs(idx, accounts, tmp)

        for i in range(len(accounts)):
            if i in self.visited:
                continue
            tmp = set()
            dfs(i, accounts, tmp)
            self.res.append([accounts[i][0]] + list(tmp))

        return self.res


test = Solution()
print test.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]])