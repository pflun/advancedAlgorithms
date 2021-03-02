# -*- coding: utf-8 -*-
# 给一个map
# {1，[‘A’,'B','C']},
# {2, ['D','E','F']}
# ...
# {0，['X','Y','Z']}
# 按一次1 返回A，连续两次返回B， 连续四次重新返回A
# 输入一组数字，不清楚之间间隔，返回所有可能的字符串数组。
# 例如： 11 -> "AA", "B"
#        1112 -> "AAAD", "ABD", 'BAD', 'CD'
class Solution(object):
    def letterCombinations(self, digits):
        self.dic = {'1': ['A', 'B', 'C'], '2': ['D', 'E', 'F']}
        self.res = []

        def helper(idx, tmp):
            if idx == len(digits):
                self.res.append(''.join(tmp[:]))
                return
            # 1 -> A
            tmp += self.dic.get(digits[idx])[0]
            helper(idx + 1, tmp)
            tmp.pop()
            # 11 -> B
            if idx + 1 <= len(digits) - 1 and digits[idx + 1] == digits[idx]:
                tmp += self.dic.get(digits[idx])[1]
                helper(idx + 2, tmp)
                tmp.pop()
            # 111 -> C
            if idx + 2 <= len(digits) - 1 and digits[idx + 1] == digits[idx] and digits[idx + 2] == digits[idx]:
                tmp += self.dic.get(digits[idx])[2]
                helper(idx + 3, tmp)
                tmp.pop()
        helper(0, [])
        return self.res

test = Solution()
print test.letterCombinations('11')
print test.letterCombinations('1112')