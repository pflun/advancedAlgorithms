# Input [[Bart, brother, List],[Bart, son Homer],[Marge, wife, Homer],[Lisa, daughter, Homer]], and two given names
# Output [Bart son Homer, Bart brother Lisa daughter Homer]
class Solution(object):
    def relationships(self, relationships, start, end):
        self.res = []
        self.r = []
        dict = {}
        for r in relationships:
            if r[0] not in dict:
                dict[r[0]] = {}
            dict[r[0]][r[2]] = r[1]

        visited = set()

        def dfs(curr, end, visited, tmp, dict):
            if curr in visited:
                return
            if curr == end:
                self.r.append(tmp[:])
                return
            for k, v in dict[curr].items():
                visited.add(curr)
                tmp += [v] + [k]
                dfs(k, end, visited, tmp, dict)
                tmp.pop()
                tmp.pop()
                visited.remove(curr)

        dfs(start, end, visited, [start], dict)
        for r in self.r:
            self.res.append(' '.join(r))
        return self.res

test = Solution()
print test.relationships([['Bart', 'brother', 'Lisa'],
                          ['Bart', 'son', 'Homer'],
                          ['Marge', 'wife', 'Homer'],
                          ['Lisa', 'daughter', 'Homer']], 'Bart', 'Homer')