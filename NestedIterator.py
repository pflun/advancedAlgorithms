# -*- coding: utf-8 -*-
# https://leetcode.com/problems/flatten-nested-list-iterator/discuss/80147/Simple-Java-solution-using-a-stack-with-explanation
# prepareStack尝试flatten一个可能的list（可能flat成数字，也有可能还是list或mixed），reverse flatten这样stack最右边永远是最先出的（更左的）
# hasNext如果当前要pop的是list，就flat掉，直到stack最右边是int
# next每次call hasNext先flat出至少一个int，然后pop就行
class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        self.prepareStack(nestedList)

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            return None
        return self.stack.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack and type(self.stack[-1]) == list:
            self.prepareStack(self.stack.pop())
        return True if len(self.stack) != 0 else False

    def prepareStack(self, nestedList):
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

test = NestedIterator([[1,1],2,[1,1]])
print test.next()
print test.next()
print test.next()
print test.next()
print test.next()