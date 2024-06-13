class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        return sum(abs(seats[i] - students[i]) for i in range(len(seats)))

test = Solution()
print test.minMovesToSeat([3,1,5], [2,7,4])
print test.minMovesToSeat([4,1,5,9], [1,3,2,6])
print test.minMovesToSeat([2,2,6,6], [1,3,2,6])