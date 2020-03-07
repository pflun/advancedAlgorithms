class ProductOfNumbers(object):

    def __init__(self):
        self.res = []
        self.zeros = []
        self.idx = 0
        self.nums = []

    def add(self, num):
        self.nums.append(num)
        if num == 0:
            self.zeros.append(self.idx)
            if len(self.res) == 0:
                self.res.append(1)
            else:
                self.res.append(self.res[-1])
        else:
            if len(self.res) == 0:
                self.res.append(num)
            else:
                self.res.append(self.res[-1] * num)

        self.idx += 1

    def getProduct(self, k):
        t = len(self.res) - k
        for z in self.zeros:
            if t <= z:
                return 0

        if k == len(self.nums):
            return self.res[-1]

        return self.res[-1] / self.res[len(self.res) - 1 - k]

productOfNumbers = ProductOfNumbers()
productOfNumbers.add(3)
productOfNumbers.add(0)
productOfNumbers.add(2)
productOfNumbers.add(5)
productOfNumbers.add(4)
print productOfNumbers.getProduct(2)
print productOfNumbers.getProduct(3)
print productOfNumbers.getProduct(4)
print productOfNumbers.getProduct(5)
productOfNumbers.add(8)
print productOfNumbers.getProduct(2)
# ["ProductOfNumbers","add","getProduct","getProduct","add","add","getProduct","add","getProduct","add","getProduct","add","getProduct","getProduct","add","getProduct"]
# [[],[7],[1],[1],[4],[5],[3],[4],[4],[3],[4],[8],[1],[6],[2],[3]]
# [null,null,7,7,null,null,140,null,560,null,240,null,8,13440,null,48]
# print productOfNumbers.add(7)
# print productOfNumbers.getProduct(1)
# print productOfNumbers.getProduct(1)
# print productOfNumbers.add(4)
# print productOfNumbers.add(5)
# print productOfNumbers.getProduct(3)
# print productOfNumbers.add(4)
# print productOfNumbers.getProduct(4)
# print productOfNumbers.add(3)
# print productOfNumbers.getProduct(4)
# print productOfNumbers.add(8)
# print productOfNumbers.getProduct(1)
# print productOfNumbers.getProduct(6)
# print productOfNumbers.add(2)
# print productOfNumbers.getProduct(3)
# ["ProductOfNumbers","add","add","add","getProduct","add","add","add","getProduct","getProduct","getProduct","add","add"]
# [[],[0],[0],[9],[3],[8],[3],[8],[5],[4],[6],[8],[8]]
# [null,null,null,null,0,null,null,null,0,1728,0,null,null]