# 2747. Count Zero Request Servers
class Solution(object):
    # TLE, sliding window using a map to maintain unique servers with requests
    def countServers(self, n, logs, x, queries):
        # time => [server_id]
        dic = {}
        for l in logs:
            dic[l[1]] = dic.get(l[1], []) + [l[0]]
        res = []
        for q in queries:
            start = q - x
            end = q
            received = set()
            for i in range(start, end + 1):
                if i in dic:
                    # append list to set, add received request server_id
                    received.update(dic[i])
            res.append(n - len(received))
        return res

test = Solution()
print test.countServers(3, [[1,3],[2,6],[1,5]], 5, [10,11])
print test.countServers(3, [[2,4],[2,1],[1,2],[3,1]], 2, [3,4])