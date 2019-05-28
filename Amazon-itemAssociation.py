# -*- coding: utf-8 -*-

class Solution(object):

    def itemAssociation(self, friends):
        friends.sort()
        counter = 0
        groups = []
        res = []
        visited = [False] * len(friends)

        for i in range(len(friends)):
            if not visited[i]:
                tmp = self.dfs(friends, i, visited, set(friends[i]))
                groups.append(list(tmp))
                counter += 1

        # 拿到最长的集合
        for group in groups:
            if len(group) > len(res):
                res = group
        return res

    def dfs(self, friends, curr, visited, tmp):
        if visited[curr]:
            return
        # 第一个最早就用掉了，所以从1开始
        for i in range(1, len(friends)):
            # [1, 2]的2 == [2, 3]的2
            if not visited[i] and friends[curr][1] == friends[i][0]:
                visited[curr] = True
                tmp.add(friends[i][1])
                self.dfs(friends, i, visited, tmp)
        visited[curr] = True
        return tmp

    def itemAssociation2(self, friends):
        groups = [set(friends[0])]
        res = []

        for i in range(len(friends)):
            flag = False
            # 对于每一个set，比如set(['T1', 'T2']), set(['T4', 'T5'])]
            for group in groups:
                # 如果[T2, T3]的2 在 set(['T1', 'T2']) 里，就往里加 T3
                if friends[i][0] in group:
                    group.add(friends[i][1])
                    flag = True

            # 如果['T4', 'T5']前面没加入任何set，就新建个set，加入groups
            if flag is False:
                groups.append(set(friends[i]))

        for group in groups:
            if len(group) > len(res):
                res = list(group)

        return res


test = Solution()
print test.itemAssociation2([['T1', 'T2'], ['T2', 'T3'], ['T4', 'T5'], ['T5', 'T6'], ['T3', 'T7']])