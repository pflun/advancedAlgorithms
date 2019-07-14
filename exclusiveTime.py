class Solution(object):
    def exclusiveTime(self, n, logs):
        res = [0 for _ in range(n)]
        queue = []
        preId, preStatus, preT = 0, '', 0

        for log in logs:
            id, status, t = self.getLog(log)
            if status == 'start':
                queue.append(log)
                res[preId] += t - preT
            elif status == 'end':
                preId = self.getLog(queue.pop())[0]
                if preId == id:
                    res[id] += t - preT + 1
            preStatus, preT = status, t

        return res

    def getLog(self, s):
        s = s.split(":")
        return int(s[0]), s[1], int(s[2])

test = Solution()
print test.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"])