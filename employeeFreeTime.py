# Treat as merge intervals for all employees
# Line sweep find free times between merged intervals
class Solution(object):
    def employeeFreeTime(self, schedule):
        res, free = [], []
        schedule = [item for sublist in schedule for item in sublist]
        intervals = sorted(schedule, key=lambda x: x[0])
        for interval in intervals:
            # first interval or no overlap
            if len(res) == 0 or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                # update last interval
                res[-1][1] = max(res[-1][1], interval[1])

        prev = res[0][1]
        for r in res[1:]:
            free.append([prev, r[0]])
            prev = r[1]

        return free

test = Solution()
print test.employeeFreeTime([[[1,2],[5,6]],[[1,3]],[[4,10]]])
print test.employeeFreeTime([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]])