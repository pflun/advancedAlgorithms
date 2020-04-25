# -*- coding: utf-8 -*-
class Solution(object):
    # 加对称数字，注意最外层不能是0
    def findStrobogrammatic2(self, n):
        if n == 0:
            return ['']
        elif n == 1:
            return ['0', '1', '8']
        self.res = []
        self.dic = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
        if n % 2 == 0:
            self.helper('', n)
        else:
            self.helper('0', n - 1)
            self.helper('1', n - 1)
            self.helper('8', n - 1)
        return self.res

    def helper(self, tmp, n):
        if n == 0:
            if tmp[0] != '0':
                self.res.append(tmp)
            return
        for k, v in self.dic.items():
            tmp = k + tmp + v
            self.helper(tmp, n - 2)
            tmp = tmp[1:-1]

    # missed edge case: n = 4:   1001, 6009, 8008, 9006...
    def findStrobogrammatic(self, n):
        res = [[''], ['0', '1', '8']]
        if n == 0:
            return res[0]
        elif n == 1:
            return res[1]
        for i in range(2, n + 1):
            tmp = []
            for r in res[i - 2]:
                tmp.append('1' + r + '1')
                tmp.append('6' + r + '9')
                tmp.append('8' + r + '8')
                tmp.append('9' + r + '6')
            res.append(tmp)
        return res[-1]

test = Solution()
print test.findStrobogrammatic2(4)