class Solution(object):
    def minOperations(self, boxes):
        res = [0 for _ in range(len(boxes))]
        for i in range(len(boxes)):
            tmp = 0
            for j in range(len(boxes)):
                if i == j:
                    continue
                if boxes[j] == '1':
                    tmp += abs(i - j)
            res[i] = tmp
        return res

test = Solution()
print test.minOperations("110")
print test.minOperations("001011")