# -*- coding: utf-8 -*-
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

    # https://leetcode.com/problems/accounts-merge/solutions/109157/java-c-union-find/
    def accountsMergeUnionFind(self, accounts):
        self.dic = {}
        email_to_name = {} # john_newyork@mail.com => John (忽略，不是这题的关键)
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in self.dic:
                    self.dic[email] = email
                email_to_name[email] = name # john_newyork@mail.com => John
                self.union(account[1], email)  # account[1]: the first email
        # 到这里完成了account[2:] 指向 account[1] 默认1是老大
        self.merged = {}
        for email in self.dic.keys():
            # 对于每一个email找到老大
            parent = self.find(email)
            # 老大 => [小弟1，小弟2 ...]
            self.merged[parent] = self.merged.get(parent, []) + [email]
        return [[email_to_name[root]] + sorted(emails) for (root, emails) in self.merged.items()]

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
print test.accountsMergeUnionFind([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]])
# 改变顺序，UF should work as expected
print test.accountsMergeUnionFind([["John", "john00@mail.com", "johnsmith@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]])