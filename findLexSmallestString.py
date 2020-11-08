class Solution(object):
    # TLE
    def findLexSmallestString(self, s, a, b):
        queue = [s]
        visited = set()
        res = s
        while queue:
            curr = queue.pop(0)
            visited.add(curr)
            first = ''
            for i in range(len(curr)):
                if i % 2 != 0:
                    c1 = str((int(curr[i]) + a) % 10)
                else:
                    c1 = curr[i]
                first += c1
            second = curr[len(curr) - b:] + curr[:len(curr) - b]
            if res > first:
                res = first
            if res > second:
                res = second
            if first not in visited:
                queue.append(first)
            if second not in visited:
                queue.append(second)
        return res

    # still not work
    def findLexSmallestString2(self, s, a, b):
        self.visited = set()
        self.res = s

        def dfs(curr, a, b):
            if curr in self.visited:
                return
            first = ''
            for i in range(len(curr)):
                if i % 2 != 0:
                    c1 = str((int(curr[i]) + a) % 10)
                else:
                    c1 = curr[i]
                first += c1
            second = curr[len(curr) - b:] + curr[:len(curr) - b]
            if self.res > first:
                self.res = first
            if self.res > second:
                self.res = second
            dfs(first, a, b)
            dfs(second, a, b)

        dfs(s, a, b)
        return self.res

test = Solution()
print test.findLexSmallestString("5525", 9, 2)
print test.findLexSmallestString("74", 5, 1)
print test.findLexSmallestString("0011", 4, 2)
print test.findLexSmallestString("43987654", 7, 3)