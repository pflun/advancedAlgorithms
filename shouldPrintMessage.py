class Solution(object):
    def __init__(self):
        self.dic = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.dic:
            self.dic[message] = timestamp
            return True
        else:
            t = self.dic[message]
            if timestamp - t >= 10:
                self.dic[message] = timestamp
                return True
            else:
                return False

test = Solution()
print test.shouldPrintMessage(1, 'foo')
print test.shouldPrintMessage(3, 'foo')
print test.shouldPrintMessage(11, 'foo')
print test.shouldPrintMessage(21, 'foo')