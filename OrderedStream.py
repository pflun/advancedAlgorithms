class OrderedStream(object):
    def __init__(self, n):
        self.queue = [None for _ in range(n)]
        self.ptr = 0

    def insert(self, idKey, value):
        self.queue[idKey - 1] = value
        if self.ptr < idKey - 1:
            return []
        res = []
        while self.ptr < len(self.queue) and self.queue[self.ptr]:
            res.append(self.queue[self.ptr])
            self.ptr += 1
        return res