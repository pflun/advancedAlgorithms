class Solution(object):
    # simply simulate, no need to BFS as below
    def reinitializePermutation(self, n):
        queue = [[i for i in range(n)]]
        target = [i for i in range(n)]
        isInitial = True
        # visited = set()
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                if curr == target and not isInitial:
                    return step
                if curr == target:
                    isInitial = False
                # visited.add(curr)
                curr1 = self.helper(curr)
                # if curr1 not in visited:
                queue.append(curr1)
            step += 1
        return -1

    def helper(self, curr):
        res = curr[:]
        for i in range(len(curr)):
            if i % 2 == 0:
                res[i] = curr[i / 2]
            else:
                res[i] = curr[len(curr) / 2 + (i - 1) / 2]
        return res

test = Solution()
print test.reinitializePermutation(2)
print test.reinitializePermutation(4)
print test.reinitializePermutation(6)