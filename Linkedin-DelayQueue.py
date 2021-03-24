import threading
class DelayQueue(object):
    def __init__(self):
        self.tasks = []
        self.condition = threading.Condition()

    def enqueue(self, task):
        with self.condition:
            heappush(self.tasks, task)
            self.condition.notifyAll()

    def dequeue(self):
        with self.condition:
            while True:
                if len(self.tasks) == 0:
                    self.condition.wait()
                else:
                    task = self.tasks[0]
                    if task.time <= 0:
                        return heappop(self.tasks)
                    # wait for a period of time
                    self.condition.wait(task.time)