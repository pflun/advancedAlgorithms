# -*- coding: utf-8 -*-
from collections import defaultdict

# ==========================================
# 解法一： DFS
# ==========================================
class SolutionDFS(object):
    def countPairs(self, n, edges):
        # 1. 建图
        self.graph = defaultdict(list)
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
            
        self.visited = set()
        res = 0
        processed = 0  # 记录之前已经处理过的总人数
        
        for i in range(n):
            if i not in self.visited:
                # 找出一个新的团队，返回这个团队的人数
                self.size = 0
                self.dfs(i)
                # 截图中提到的核心公式：当前团队人数 * 之前所有团队的总人数
                res += self.size * processed
                # 更新已经统计过的人数
                processed += self.size
                
        return res

    # dfs 负责遍历连通块，并返回这个连通块的节点总数(team_size)
    def dfs(self, curr):
        if curr in self.visited:
            return
        self.visited.add(curr)
        self.size += 1
        for neighbor in self.graph[curr]:
            self.dfs(neighbor)


# ==========================================
# 解法二： Union Find (并查集) - 参照你的模版
# ==========================================
class SolutionUF(object):
    # O(n) 返回老大哥
    def find(self, x):
        parent = self.dic[x]
        while parent != self.dic[parent]:
            parent = self.dic[parent]
        return parent

    # 合并老大哥
    def union(self, master, branch):
        fa_master = self.find(master)
        fa_branch = self.find(branch)
        if fa_master != fa_branch:
            self.dic[fa_branch] = fa_master

    def countPairs(self, n, edges):
        # 1. 初始化字典：每个人的初始老大哥都是自己
        self.dic = {i: i for i in range(n)}
        
        # 2. 合并所有连通关系
        for u, v in edges:
            self.union(u, v)
            
        # 3. 统计每个老大哥手下有多少人 (即每个 team 的 size)
        team_sizes = {}
        for i in range(n):
            # 找到老大哥，然后老大哥的team size += 1
            root = self.find(i)
            team_sizes[root] = team_sizes.get(root, 0) + 1
            
        # 4. 用之前提过的巧妙公式计算 pairs
        res = 0
        processed = 0
        
        for team_size in team_sizes.values():
            res += team_size * processed
            processed += team_size
            
        return res

# 测试代码
if __name__ == "__main__":
    dfs_sol = SolutionDFS()
    uf_sol = SolutionUF()
    
    # 截图中的 Example 2
    n = 5
    edges = [[0,1], [2,3], [0,4]]
    
    print "DFS Output:", dfs_sol.countPairs(n, edges)  # 预期输出: 6
    print "UF Output:", uf_sol.countPairs(n, edges)    # 预期输出: 6