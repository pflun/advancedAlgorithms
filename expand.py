# convert_s: "{a,b}c{d,e}f" => [[a, b], c, [d, e], f]
# tmp stores prev result, backtracking
class Solution(object):
    def expand(self, s):
        self.res = []
        self.convert_s = []

        def dfs(tmp, i):
            if i == len(self.convert_s):
                self.res.append(''.join(tmp))
                return
            if type(self.convert_s[i]) == list:
                for c in self.convert_s[i]:
                    tmp.append(c)
                    dfs(tmp, i + 1)
                    tmp.pop()
            elif type(self.convert_s[i]) == str:
                tmp.append(self.convert_s[i])
                dfs(tmp, i + 1)
                tmp.pop()

        i = 0
        while i < len(s):
            if s[i] == '{':
                j = s.find('}', i)
                curr = s[i + 1:j].split(',')
                self.convert_s.append(curr)
                i = j + 1
            elif s[i].isalpha():
                self.convert_s.append(s[i])
                i += 1
        dfs([], 0)
        return self.res

test = Solution()
print test.expand("{a,b}c{d,e}f")
print test.expand("abcd")