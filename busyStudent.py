class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        startTime.sort()
        endTime.sort()
        t = 1
        curr = 0
        while t <= queryTime:
            while startTime and t == startTime[0]:
                curr += 1
                startTime.pop(0)
            if t == queryTime:
                return curr
            while endTime and t == endTime[0]:
                curr -= 1
                endTime.pop(0)
            t += 1
        return curr

test = Solution()
print test.busyStudent([1,2,3], [3,2,7], 4)
print test.busyStudent([4], [4], 4)
print test.busyStudent([4], [4], 5)
print test.busyStudent([1,1,1,1], [1,3,2,4], 7)
print test.busyStudent([9,8,7,6,5,4,3,2,1], [10,10,10,10,10,10,10,10,10], 5)