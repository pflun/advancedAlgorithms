# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight, bottomLeft):
#        """
#        :type topRight: Point
#		 :type bottomLeft: Point
#        :rtype bool
#        """
#
# class Point(object):
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y

class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        """
        :type sea: Sea
        :type topRight: Point
        :type bottomLeft: Point
        :rtype: integer
        """
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        # at one point
        elif topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
        midX = (topRight.x + bottomLeft.x) / 2
        midY = (topRight.y + bottomLeft.y) / 2
        return self.countShips(sea, Point(midX, midY), bottomLeft) + self.countShips(sea, Point(midX, topRight.y), Point(bottomLeft.x, midY+1)) + self.countShips(sea, Point(topRight.x, midY), Point(midX+1, bottomLeft.y)) + self.countShips(sea, topRight, Point(midX+1, midY+1))