class Solution(object):
    def minTime(self, n, edges, hasApple):
        self.res = 0
        graph = {}
        apple = set()
        for e in edges:
            if e[0] in graph:
                graph[e[0]].append(e[1])
            else:
                graph[e[0]] = [e[1]]
        for i in range(n):
            if hasApple[i]:
                apple.add(i)
        self.helper(graph, apple, 0)
        return self.res

    def helper(self, graph, apple, idx):
        if idx not in graph:
            if idx in apple:
                return True
            else:
                return False
        arr = []
        for n in graph[idx]:
            arr.append(self.helper(graph, apple, n))
        curr = False
        for a in arr:
            if a:
                curr = True
                self.res += 2
        # if curr has apple, return True
        if idx in apple:
            curr = True
        return curr

test = Solution()
print test.minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False])
print test.minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,False,True,False])
print test.minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,False,False,False,False,False])
