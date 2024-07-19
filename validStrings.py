class Solution(object):
    def validStrings(self, n):
        self.res = []
        self.binary = ["0", "1"]

        def dfs(n, tmp):
            if len(tmp) == n:
                # deep copy
                self.res.append("".join(tmp[:]))
                return

            for i in range(len(self.binary)):
                if self.binary[i] == "0" and tmp and tmp[-1] == "0":
                    continue
                tmp.append(self.binary[i])
                dfs(n, tmp)
                tmp.pop()

        dfs(n, [])
        return self.res

test = Solution()
print test.validStrings(3)
print test.validStrings(1)