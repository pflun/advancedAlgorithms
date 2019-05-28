# You're asked to randomly assign headcount to a list of months, a group of research scientists will provide you a list of weights
# based on their model, since some months are getting higher turnover rate than others, so they will more likely
# get the headcount (weighted higher) the chance of each month being assigned is proportional to its weight
# Your inputs are, m for months, i.e. ['jan', 'feb', 'nov'] and w for weight, i.e. [1,3,4], return the month, say "nov"
# follow-up questions: how to modify your code if you plan to assign 20,000 headcounts?
import random
class Solution(object):
    def __init__(self, m, w):
        self.months = m
        self.candidates = []
        self.sum = 0
        for n in w:
            self.sum += n
            if len(self.candidates) == 0:
                self.candidates.append(n)
            else:
                self.candidates.append(n + self.candidates[-1])

    def randomAssignHeadcount(self):
        r = random.randint(0, self.sum)
        return self.months[self.binarySearch(r)]

    # find smallest element that larger than target
    def binarySearch(self, r):
        low = 0
        high = len(self.candidates) - 1
        while low < high:
            mid = (low + high) / 2
            if self.candidates[mid] <= r:
                low = mid + 1
            else:
                high = mid
        return low if self.candidates[low] > r else high


obj = Solution(['jan', 'feb', 'nov'], [1,3,2])
print obj.randomAssignHeadcount()