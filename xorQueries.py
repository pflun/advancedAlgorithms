# Because a ^ b ^ a = b
# query(l, r) = query(0, r + 1) - query(0, l)
class Solution(object):
    def xorQueries(self, arr, queries):
        prefix = [1]
        for i in range(len(arr)):
            prefix.append(prefix[-1] ^ arr[i])
        res = []
        for q in queries:
            l = q[0]
            r = q[1]
            res.append(prefix[r + 1] ^ prefix[l])
        return res

test = Solution()
print test.xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]])
print test.xorQueries([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]])