import random
class Solution(object):
    # wrong solution and Python TLE
    def minimumTimeRequired(self, jobs, k):
        sumVal = 0
        for job in jobs:
            sumVal += job
        lo = 1
        hi = sumVal
        while lo <= hi:
            mid = (hi - lo) / 2 + lo
            if self.helperFunc(jobs, k, mid):
                hi = mid -1
            else:
                lo = mid + 1
        return lo

    def helperFunc(self, jobs, k, time):
        for _ in range(30001):
            for i in range(len(jobs)):
                randIdx = random.randint(0, len(jobs) - 1)
                jobs[randIdx], jobs[i] = jobs[i], jobs[randIdx]
            if self.isPossible(jobs, k, time):
                return True
        return False

    def isPossible(self, jobs, k, time):
        cnt = 1
        currTime = 0
        i = 0
        while i < len(jobs):
            if jobs[i] > time:
                return False
            if currTime + jobs[i] > time:
                cnt += 1
                currTime = 0
            else:
                currTime += jobs[i]
                i += 1
        return True if cnt <= k else False

test = Solution()
print test.minimumTimeRequired([3,2,3], 3)
print test.minimumTimeRequired([1,2,4,7,8], 2)
