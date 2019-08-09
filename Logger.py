class Logger(object):
    def __init__(self):
        self.dic = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.dic:
            self.dic[message] = timestamp
            return True
        else:
            prevT = self.dic[message]
            if timestamp - prevT < 10:
                return False
            else:
                self.dic[message] = timestamp
                return True