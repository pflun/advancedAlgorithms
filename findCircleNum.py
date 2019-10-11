class Solution(object):
    def findCircleNum(self, M):
        self.dic = {}
        for i in range(len(M)):
            for j in range(i + 1, len(M)):
                if M[i][j] == 1:
                    self.union(i, j)
        # find how many root
        circles = set()
        for i in range(len(M)):
            circles.add(self.find(i))
        return len(circles)

    def find(self, x):
        parent = self.dic[x]
        while parent != self.dic[parent]:
            parent = self.dic[parent]
        return parent

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.dic[rootx] = rooty