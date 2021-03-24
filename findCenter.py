class Solution(object):
    def findCenter2(self, edges):
        dic = {}
        for e in edges:
            dic[e[0]] = dic.get(e[0], []) + [e[1]]
            dic[e[1]] = dic.get(e[1], []) + [e[0]]
            if len(dic[e[0]]) == len(edges):
                return e[0]
            if len(dic[e[1]]) == len(edges):
                return e[1]

    def findCenter(self, edges):
        e0 = set(edges[0])
        e1 = set(edges[1])
        for k in e0:
            if k in e1:
                return k


test = Solution()
print test.findCenter([[1,2],[2,3],[4,2]])
print test.findCenter([[1,2],[5,1],[1,3],[1,4]])