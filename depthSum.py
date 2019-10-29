# https://www.youtube.com/watch?v=KP538-uPtz0
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
   def isInteger(self, x):
       if type(x) == int:
           return True
       else:
           return False
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        if not nestedList:
            return None
        return self.dfs(nestedList, 1)

    def dfs(self, nestedList, depth):
        res = 0
        for num in nestedList:
            if NestedInteger().isInteger(num):
                res += NestedInteger().getInteger(num) * depth
                # res += num * depth
            else:
                res = self.dfs(NestedInteger().getList(), depth + 1)

        return res

class Solution2(object):
    def depthSum(self, nestedList):
        self.res = 0

        def dfs(A, depth):
            if type(A) == int:
                self.res += A * depth
            else:
                for a in A:
                    dfs(a, depth + 1)

        dfs(nestedList, 0)

        return self.res

test = Solution2()
print test.depthSum([1,[4,[6]]])