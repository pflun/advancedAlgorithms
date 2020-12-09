class MyCircularDeque(object):

    def __init__(self, k):
        self.queue = [-1 for _ in range(k)]
        self.front = 0
        self.rear = 0
        self.capacity = k
        self.size = 0

    def insertFront(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self.queue[self.front] = value
        else:
            self.front = (self.front - 1) % self.capacity
            self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.queue[self.front] = -1
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        # imagine init insertFront, deleteFront, now your front pointer at 1 and rear at 0, need to sync front and rear
        if self.isEmpty():
            self.front = self.rear
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.queue[self.rear] = -1
        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1
        if self.isEmpty():
            self.rear = self.front
        return True

    def getFront(self):
        return self.queue[self.front]

    def getRear(self):
        return self.queue[self.rear]

    def isEmpty(self):
        return True if self.size == 0 else False

    def isFull(self):
        return True if self.size == self.capacity else False