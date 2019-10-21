class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) <= 2:
            return True
        self.diag = 0
        for i in range(len(coordinates) - 1):
            p1 = coordinates[i]
            p2 = coordinates[i + 1]
            if p2[0] - p1[0] != 0:
                if self.diag == 0:
                    self.diag = (p2[1] - p1[1]) / (p2[0] - p1[0])
                    continue
                if self.diag != (p2[1] - p1[1]) / (p2[0] - p1[0]):
                    return False
            else:
                if self.diag == 0:
                    self.diag = float('inf')
                    continue
                if self.diag != float('inf'):
                    return False
        return True

test = Solution()
print test.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])
print test.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])
print test.checkStraightLine([[-1,1],[-6,-4],[-6,2],[2,0],[-1,-2],[0,-4]])