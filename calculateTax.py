class Solution(object):
    def calculateTax(self, brackets, income):
        res = 0
        prev = 0
        for b in brackets:
            if income == 0:
                break
            next = b[0] - prev
            if income >= next:
                res += next * b[1] / float(100)
                income -= next
            else:
                res += income * b[1] / float(100)
                income = 0
            prev = b[0]
        return res

test = Solution()
print test.calculateTax([[3,50],[7,10],[12,25]], 10)
print test.calculateTax([[1,0],[4,25],[5,50]], 2)
print test.calculateTax([[2,50]], 0)