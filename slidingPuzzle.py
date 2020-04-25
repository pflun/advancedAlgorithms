# -*- coding: utf-8 -*-
class Solution(object):
    def slidingPuzzle(self, board):
        # position can be swapped to
        self.dir = [[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]
        self.visited = set()
        target = "123450"
        start = ""
        for i in range(len(board)):
            for j in range(len(board[0])):
                start += str(board[i][j])
        queue = [start]
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                self.visited.add(curr)
                if curr == target:
                    return step
                for i in range(len(self.dir)):
                    for d in self.dir[i]:
                        next = self.swap(curr, i, d)
                        if next not in self.visited:
                            queue.append(next)
            step += 1

        return -1

    def swap(self, curr, i, d):
        res = ''
        for j in range(len(curr)):
            if j == i:
                res += curr[d]
            elif j == d:
                res += curr[i]
            else:
                res += curr[j]
        return res

test = Solution()
print test.slidingPuzzle([[1,2,3],[4,0,5]])
# -1 这个test case有问题，return 1 要改
print test.slidingPuzzle([[1,2,3],[5,4,0]])
print test.slidingPuzzle([[4,1,2],[5,0,3]])
