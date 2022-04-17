class Solution(object):
    def calculate1(self, arr):
        dic = {}
        curr = arr[0]
        for a in arr[1]:
            vals = [x.strip() for x in a.split("=")]
            if vals[1].isdigit():
                dic[vals[0]] = int(vals[1])
            else:
                dic[vals[0]] = vals[1]

        while type(curr) != int:
            curr = dic[curr]
        return curr

    def calculate2(self, arr):
        dic = {}
        target = arr[0]
        def parse(t):
            if t.isdigit():
                return int(t)
            else:
                return t

        for a in arr[1]:
            vals = [x.strip() for x in a.split("=")]
            if '+' in vals[1]:
                tmp = [x.strip() for x in vals[1].split("+")]
                dic[vals[0]] = [[parse(tmp[0]), parse(tmp[1])], []]
            elif '-' in vals[1]:
                tmp = [x.strip() for x in vals[1].split("-")]
                dic[vals[0]] = [[parse(tmp[0])], [parse(tmp[1])]]
            else:
                if vals[1].isdigit():
                    dic[vals[0]] = int(vals[1])
                else:
                    dic[vals[0]] = [[vals[1]], []]

        def dfs(curr):
            if type(curr) == int:
                return curr
            if curr in dic and type(dic[curr]) == int:
                return dic[curr]
            next = dic[curr]
            calculated = 0
            for n in next[0]:
                calculated += dfs(n)
            for n in next[1]:
                calculated -= dfs(n)
            return calculated
        return dfs(target)

    def hasCycle(self, arr):
        dic = {}
        target = arr[0]

        def parse(t):
            if t.isdigit():
                return int(t)
            else:
                return t

        for a in arr[1]:
            vals = [x.strip() for x in a.split("=")]
            if '+' in vals[1]:
                tmp = [x.strip() for x in vals[1].split("+")]
                dic[vals[0]] = [[parse(tmp[0]), parse(tmp[1])], []]
            elif '-' in vals[1]:
                tmp = [x.strip() for x in vals[1].split("-")]
                dic[vals[0]] = [[parse(tmp[0])], [parse(tmp[1])]]
            else:
                if vals[1].isdigit():
                    dic[vals[0]] = int(vals[1])
                else:
                    dic[vals[0]] = [[vals[1]], []]

        def dfs(curr, visited):
            if curr in visited:
                return "IMPOSSIBLE"
            visited.add(curr)
            if type(curr) == int:
                return curr
            if curr in dic and type(dic[curr]) == int:
                return dic[curr]
            next = dic[curr]
            calculated = 0
            for n in next[0]:
                visited_copy = set(visited)
                tmp = dfs(n, visited_copy)
                if tmp == "IMPOSSIBLE":
                    return tmp
                calculated += tmp
            for n in next[1]:
                visited_copy = set(visited)
                tmp = dfs(n, visited_copy)
                if tmp == "IMPOSSIBLE":
                    return tmp
                calculated -= tmp
            return calculated

        return dfs(target, set())

test = Solution()
print test.calculate1(["T2", ["T1 = 1", "T2 = T3", "T3 = T1"]])
print test.calculate2(["T2", ["T1 = 1", "T2 = 2 + T4", "T3 = T1 - 4", "T4 = T1 + T3"]])
print test.calculate2(["t1", ["t1 = t2 + t3", "t2 = t4 + t3", "t3 = 5", "t4 = 1"]])
print test.hasCycle(["t1", ["t1 = t2 + t3", "t2 = t4 + t3", "t3 = 5", "t4 = 1"]])
print test.hasCycle(["t1", ["t1 = t2", "t2 = t3", "t3 = t4", "t4 = t1"]])
print test.hasCycle(["t1", ["t1 = t2 + t3", "t2 = t3", "t3 = 1"]])
print test.hasCycle(["t3", ["t2 = 2", "t3 = t4 + t5", "t4 = t5", "t5 = t4"]])