# -*- coding: utf-8 -*-
# 第二问: setCell是formula， e.g. setCell("A1", "=B1+5")。可以假设只有+，没有-*%。formula肯定是=开头
# 这里要想到在setCell的时候要直接更新所有依赖这个cell的cell。e.g.更新B1的时候A1也需要更新，就跟spreadseet是一样的。
# 解法就是记录每一个cell的被依赖关系，e.g. B1的被依赖cell是{"A1"}，然后当B1的值被修改时，依次修改所有被依赖的cell
# cell的值有时是formula有时是int，这个比较麻烦，建议提前写熟练
# 第三问: circular dependency detection。如果setCell的时候出现circular dependency的话能探测到
class Spreadsheet(object):

    def __init__(self, rows):
        self.dic = {}


    def setCell(self, cell, value):
        self.dic[cell] = value


    def resetCell(self, cell):
        self.dic[cell] = 0


    def getValue(self, formula):
        A, B = formula[1:].split('+')
        return self.helper(A) + self.helper(B)

    def helper(self, num):
        if num.isdigit():
            return int(num)
        else:
            return self.dic.get(num, 0)

test = Spreadsheet(3)
print test.getValue('=5+7')
print test.setCell("A1", 10)
print test.getValue('=A1+6')
print test.setCell("B2", 15)
print test.getValue('=A1+B2')
print test.resetCell('A1')
print test.getValue('=A1+B2')
