import bisect
class SnapshotArray(object):
    def __init__(self, length):
        self.A = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0
        self.n = length

    def set(self, index, val):
        self.A[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        i = bisect.bisect(self.A[index], [snap_id + 1]) - 1
        return self.A[index][i][1]

test = SnapshotArray(3)
print test.set(0, 5)
print test.snap()
print test.set(0, 6)
print test.get(0, 0)