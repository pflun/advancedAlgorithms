from datetime import date
class Solution(object):
    def daysBetweenDates(self, date1, date2):
        d1 = date1.split('-')
        d2 = date2.split('-')
        return abs((date(int(d1[0]), int(d1[1]), int(d1[2])) - date(int(d2[0]), int(d2[1]), int(d2[2]))).days)

test = Solution()
print test.daysBetweenDates("2019-06-29", "2019-06-30")
print test.daysBetweenDates("2020-01-15", "2019-12-31")