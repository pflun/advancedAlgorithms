# -*- coding: utf-8 -*-
# User Journey Paths (Action Log Trie Summary)
# Input
# Logs in format
# (user_id, time, action)
# 100  1000  A
# 300  1150  A
# 200  1200  B
# 100  1200  B
# 100  1300  C
# 200  1400  A
# 300  1500  B
# 300  1550  B
# 100  1560  D
# Per-user sequences (sorted by time ascending)
# user 100: A -> B -> C -> D
# user 200: B -> A
# user 300: A -> B -> B
# Expected output
# Indented tree showing each unique path prefix and the count of distinct users who reached that node via that path:
# A (2)
#   -> B (2)
#     -> C (1)
#       -> D (1)
#     -> B (1)
# B (1)
#   -> A (1)

class TrieNode:
    def __init__(self):
        self.count = 1
        self.children = {}

class Solution(object):
    def userJourneyPaths(self, logs):
        root = TrieNode()
        dic = {}
        for log in logs:
            user_id, time, action = log[0], log[1], log [2]
            if user_id not in dic:
                dic[user_id] = {}
            dic[user_id][time] = action
        for path in dic.values():
            node = root
            for _, action in sorted(path.items()):
                if action not in node.children:
                    node.children[action] = TrieNode()
                else:
                    node.children[action].count += 1
                node = node.children[action]

        # ===== Build Trie above =====

        def dfs(node, level):
            res = []
            for action in sorted(node.children.keys()):
                child = node.children[action]
                if level == 0:
                    prefix = ""
                else:
                    prefix = " " * (level * 2) + "-> "
                
                res.append("{}{} ({})".format(prefix, action, child.count))
                res.extend(dfs(child, level + 1))
            return res

        return "\n".join(dfs(root, 0))

test = Solution()
print test.userJourneyPaths(
    [[100, 1000, 'A'],
    [300, 1150, 'A'],
    [200, 1200, 'B'],
    [100, 1200, 'B'],
    [100, 1300, 'C'],
    [200, 1400, 'A'],
    [300, 1500, 'B'],
    [300, 1550, 'B'],
    [100, 1560, 'D']]
)