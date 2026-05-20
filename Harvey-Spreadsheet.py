# -*- coding: utf-8 -*-
# /Users/zgao/Snapchat/dev/advancedAlgorithms/Spreadsheet.py
# 第二问: setCell是formula， e.g. setCell("A1", "=B1+5")。可以假设只有+，没有-*%。formula肯定是=开头
# 这里要想到在setCell的时候要直接更新所有依赖这个cell的cell。e.g.更新B1的时候A1也需要更新，就跟spreadseet是一样的。
# 解法就是记录每一个cell的被依赖关系，e.g. B1的被依赖cell是{"A1"}，然后当B1的值被修改时，依次修改所有被依赖的cell
# cell的值有时是formula有时是int，这个比较麻烦，建议提前写熟练
# 第三问: circular dependency detection。如果setCell的时候出现circular dependency的话能探测到
import collections

class Spreadsheet(object):

    def __init__(self, rows):
        self.dic = {}          # 存储每个 cell 最终的 int 值
        self.formulas = {}     # 存储每个 cell 的 raw 公式 e.g. {"A1": "=B1+5"}
        self.deps = collections.defaultdict(set) # 被依赖关系图 e.g. B1 -> {"A1"}

    def setCell(self, cell, value):
        # 1. 如果赋予的是公式
        if isinstance(value, str) and value.startswith('='):
            self.formulas[cell] = value
            A, B = value[1:].split('+')

            # 建立依赖关系: 告诉 A 和 B, "我(cell)现在依赖你们了"
            if not A.isdigit(): self.deps[A].add(cell)
            if not B.isdigit(): self.deps[B].add(cell)

        # 2. 如果赋予的是纯数字
        else:
            if cell in self.formulas:
                del self.formulas[cell] # 清除旧公式
            self.dic[cell] = int(value)

        # 3. 触发级联更新，传入一个空的 visited 集合用于探测环
        if not self.update(cell, set()):
            print "Error: Circular Dependency Detected!"

    def resetCell(self, cell):
        self.setCell(cell, 0)

    # 用来获取一个具体的 cell 的最终值
    def getValue(self, cell):
        return self.dic.get(cell, 0)

    # 递归更新函数，返回 False 表示探测到了环
    def update(self, cell, visited):
        if cell in visited:
            return False # 探测到环

        visited.add(cell)

        # 如果自己是个公式，先重新计算自己的值
        if cell in self.formulas:
            A, B = self.formulas[cell][1:].split('+')
            self.dic[cell] = self.helper(A) + self.helper(B)

        # 顺藤摸瓜，通知所有依赖我的 cell 重新计算
        for dep_cell in self.deps[cell]:
            if not self.update(dep_cell, visited):
                return False

        visited.remove(cell) # 回溯
        return True

    def helper(self, num):
        if num.isdigit():
            return int(num)
        else:
            return self.dic.get(num, 0)

test = Spreadsheet(3)
test.setCell("A1", 10)
print test.getValue("A1")  # Output: 10

test.setCell("B1", "=A1+5")
print test.getValue("B1")  # Output: 15

test.setCell("A1", 20)     # 修改A1，B1应该自动跟着变
print test.getValue("B1")  # Output: 25

test.setCell("C1", "=B1+10")
print test.getValue("C1")  # Output: 35

# 测试循环依赖 Circular Dependency
test.setCell("A1", "=C1+1") # A1 依赖 C1, C1 依赖 B1, B1 依赖 A1 -> Cycle!