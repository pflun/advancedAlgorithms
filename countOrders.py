# -*- coding: utf-8 -*-
# Doordash pickup delivery
# Assume we have already n - 1 pairs, now we need to insert the nth pair.
# To insert the first element, there are 2 * n - 1 chioces of position (两倍的P和D就是 2 * (n - 1) 头尾都可以插入所以多一个就 + 1)
# To insert the second element, there are 2 * n chioces of position (2 * n - 1基础上直接 + 1 因为头尾都可以插入)
# So there are (2 * n - 1) * 2 * n permutations. (上面两个相乘种possibility)
# Considering that delivery(i) is always after of pickup(i), we need to divide 2.
# So it's (2 * n - 1) * n.
class Solution(object):
    def countOrders(self, n):
        res = 1
        for i in range(2, n + 1):
            res = res * (i * 2 - 1) * i
        return res % 10 ** 9 + 7