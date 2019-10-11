class Solution(object):
    # brutal force
    def countVowelPermutation(self, n):
        if n == 0:
            return 0
        self.res = 0
        self.arr = ['a', 'e', 'i', 'o', 'u']

        def dfs(prev, n):
            if n == 0:
                self.res += 1
                return
            for a in self.arr:
                if prev == 'a' and a == 'e':
                    dfs('e', n - 1)
                elif prev == 'e' and a == 'a' or prev == 'e' and a == 'i':
                    dfs(a, n - 1)
                elif prev == 'i' and a != 'i':
                    dfs(a, n - 1)
                elif prev == 'o' and a == 'i' or prev == 'o' and a == 'u':
                    dfs(a, n - 1)
                elif prev == 'u' and a == 'a':
                    dfs(a, n - 1)

        for a in self.arr:
            dfs(a, n - 1)

        return self.res

test = Solution()
print test.countVowelPermutation(5)