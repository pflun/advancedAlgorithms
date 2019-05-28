# -*- coding: utf-8 -*-
# 多叉树LCA
# 这题基本和lowestCommonAncestor.py一样，就是遍历递归当前节点的下属
class Employee(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.reports = []

    def addReports(self, employee):
        self.reports.append(employee)


class Solution(object):
    def findCommonManager(self, ceo, employee1, employee2):
        if not ceo:
            return None
        if ceo == employee1 or ceo == employee2:
            return ceo

        isSupervise1 = False
        isSupervise2 = False

        # 递归当前结点的下属
        for i in range(len(ceo.reports)):
            curr = self.findCommonManager(ceo.reports[i], employee1, employee2)
            if curr == employee1:
                isSupervise1 = True
            elif curr == employee2:
                isSupervise2 = True
            elif curr is not None:
                return curr

        if isSupervise1 and isSupervise2:
            return ceo
        elif isSupervise1:
            return employee1
        elif isSupervise2:
            return employee2

        return None

boss = Employee(5, "Bill Gates")
employee1 = Employee(1, "employee1")
employee2 = Employee(2, "employee1")
employee3 = Employee(3, "employee1")
employee4 = Employee(4, "employee1")
boss.addReports(employee3)
boss.addReports(employee4)
employee3.addReports(employee1)
employee1.addReports(employee2)

test1 = Solution()
print test1.findCommonManager(boss, employee1, employee2).id