class Logger(object):
    def __init__(self):
        self.dic = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.dic:
            self.dic[message] = timestamp
            return True
        else:
            if timestamp - self.dic[message] > 10:
                self.dic[message] = timestamp
                return True
        return False