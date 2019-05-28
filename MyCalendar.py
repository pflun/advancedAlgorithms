class MyCalendar(object):

    def __init__(self):
        self.books = []

    def book(self, start, end):
        if not self.books:
            self.books.append([start, end])
            return True
        if start >= self.books[-1][1]:
            self.books.append([start, end])
            return True
        if end <= self.books[0][0]:
            self.books = [[start, end]] + self.books
            return True
        for i in range(1, len(self.books)):
            if self.books[i][0] >= end and self.books[i - 1][1] <= start:
                self.books.insert(i, [start, end])
                return True
        return False

obj = MyCalendar()
print obj.book(10,20)
print obj.book(15,25)
print obj.book(20,30)