# -*- coding: utf-8 -*-
# 385. Mini Parser
class NestedInteger(object):
   def __init__(self, value=None):
       pass

   def add(self, value):
       pass

class SolutionParser(object):
    def deserialize(self, s):
        # global pointer
        self.i = 0

        def parse():
            if s[self.i] == '[':
                self.i += 1  # 跳过左括号 '['
                ni = NestedInteger()
                while True:
                    # recursively parse whatever starting from '['
                    ni.add(parse())
                    if s[self.i] == ',':
                        self.i += 1
                        continue
                    # exit after reached ']'
                    elif s[self.i] == ']':
                        self.i += 1
                        return ni
            else:
                start = self.i
                while self.i < len(s) and (s[self.i].isdigit() or s[self.i] == '-'):
                    self.i += 1
                return NestedInteger(int(s[start:self.i]))
        return parse()