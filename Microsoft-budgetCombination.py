# -*- coding: utf-8 -*-
# 给你一个menu，是一个map，key是菜名，value是价格，比如
# "apple": 3.25,
# "chicken": 4.55,
# "cake":10.85,
#
# 然后给你一个budget，比如7.80.
# 要你给出所有菜名的combination，总价要正好符合budget，次序不重要，但不能有重复。
# 比如，如果budget是7.80，他就要求结果是[["apple", "chicken"]]，不能是[["apple", "chicken"],["chicken","apple"]]
# 比如，如果budget是6.50，他就要求结果是[["apple", "apple"]]
class Solution:
    def budgetCombination(self, menu, budget):
        self.res = []
        self.used = set()
        # corner case: 去掉单一overbudget的

        def dfs(menu, budget, tmp, prev):
            if len(tmp) > 1 and getSum(tmp) > budget:
                res = tmp[:]
                self.res.append(res[:-1])
                return
            for food, price in menu.items():
                if food in self.used:
                    continue
                self.used.add(food)
                tmp.append(food)
                dfs(menu, budget, tmp)
                tmp.pop()
                self.used.remove(food)