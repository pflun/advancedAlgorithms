# Design a register system, where the system provides API like register , deregister and sendConfirmation.
# However, due to the event size limit, only some of the registered users can be selected and the users are ranked by their register time.
# To design such a system to make the best performance
from collections import OrderedDict
class Register(object):
    def __init__(self, capacity):
        self.dic = OrderedDict()
        self.capacity = capacity

    def register(self, student):
        if self.capacity > 0:
            if student not in self.dic:
                self.dic[student] = True
                self.capacity -= 1

    def deregister(self, student):
        if student in self.dic:
            self.dic.pop(student)
            self.capacity += 1

    # Print student in order
    def sendConfirmation(self):
        for key, val in self.dic.items():
            print key

test = Register(5)
test.register('xiaoming')
test.register('xiaoming2')
test.deregister('xiaoming')
test.sendConfirmation()