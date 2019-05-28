class Solution(object):
    def numberOfBoomerangs(self, points):
        counter = 0
        for i in range(len(points)):
            dic = {}
            for j in range(len(points)):
                if i != j:
                    distance = ((points[i][0] - points[j][0]) ** 2) + ((points[i][1] - points[j][1]) ** 2)
                    dic[distance] = dic.get(distance, 0) + 1
            for key, val in dic.items():
                if val >= 2:
                    counter += val * (val - 1)

        return counter

test = Solution()
print test.numberOfBoomerangs([[0,0],[1,0],[2,0]])