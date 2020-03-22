# https://www.youtube.com/watch?v=seQnf-5hlBo
# below is brutal force, solution 2 is binary search
# binary search: https://leetcode.com/problems/my-calendar-i/discuss/423703/Java-Solution-Sorted-Calendar-Binary-Search-100-time-and-memory
class MyCalendar(object):
    def __init__(self):
        self.events = []

    def book(self, start, end):
        for e in self.events:
            first = max(e[0], start)
            second = min(e[1], end)
            if first < second:
                return False
        self.events.append([start, end])
        return True

obj = MyCalendar()
print obj.book(10,20)
print obj.book(15,25)
print obj.book(20,30)