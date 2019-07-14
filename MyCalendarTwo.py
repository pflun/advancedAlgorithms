# https://www.youtube.com/watch?v=rRMdxFA-8G4
class MyCalendarTwo(object):
    def __init__(self):
        self.booked = []
        self.overlaps = []

    def book(self, start, end):
        # conflict with overlap
        for o in self.overlaps:
            if max(start, o[0]) < min(end, o[1]):
                return False

        for b in self.booked:
            s = max(start, b[0])
            e = min(end, b[1])
            if s < e:
                self.overlaps.append([s, e])
        self.booked.append([start, end])
        return True

test = MyCalendarTwo()
test.book(10, 20) # returns true
test.book(50, 60) # returns true
test.book(10, 40) # returns true
test.book(5, 15) # returns false
test.book(5, 10) # returns true
test.book(25, 55) # returns true