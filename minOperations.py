class Solution(object):
    def minOperations(self, logs):
        res = 0
        for l in logs:
            if l == './':
                continue
            elif l == '../':
                res -=1
            else:
                res += 1
            if res < 0:
                res = 0
        return res

test = Solution()
print test.minOperations(["d1/","d2/","../","d21/","./"])
print test.minOperations(["d1/","d2/","./","d3/","../","d31/"])
print test.minOperations(["d1/","../","../","../"])
print test.minOperations(["./","wz4/","../","mj2/","../","../","ik0/","il7/"])