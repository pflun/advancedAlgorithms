# BFS + visited
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        visited = set()
        # stop => reachable stops within 1 travel
        dic = {}
        for r in routes:
            for s in r:
                if s in dic:
                    dic[s] = dic.get(s) + r
                else:
                    # except self stop, you've already at #2, you don't want to go to #2 again
                    tmp = r[:]
                    tmp.remove(s)
                    dic[s] = tmp
        step = 0
        queue = dic[S]
        while queue:
            step += 1
            size = len(queue)
            for _ in range(size):
                tmp = queue.pop(0)
                # found target
                if tmp == T:
                    return step
                if tmp not in visited:
                    # add stops within 1 travel to queue
                    queue += dic[tmp]
                    visited.add(tmp)
        return dic

test = Solution()
print test.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6)