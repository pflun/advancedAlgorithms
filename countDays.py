class Solution(object):
    def countDays(self, days, meetings):
        # merge intervals
        mergedMeetings = []
        meetings.sort()
        for interval in meetings:
            # first interval or no overlap
            if len(mergedMeetings) == 0 or mergedMeetings[-1][1] < interval[0]:
                mergedMeetings.append(interval)
            else:
                # update last interval
                mergedMeetings[-1][1] = max(mergedMeetings[-1][1], interval[1])
        # count how many days has meeting then use total days - meeting days
        hasMeetingDay = 0
        for m in mergedMeetings:
            hasMeetingDay += m[1] - m[0] + 1
        return days - hasMeetingDay

test = Solution()
print test.countDays(10, [[5,7],[1,3],[9,10]])
print test.countDays(5, [[2,4],[1,3]])
print test.countDays(6, [[1,6]])
print test.countDays(10, [[1,2]])