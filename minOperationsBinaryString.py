# -*- coding: utf-8 -*-
# 其实只有两种可能 0101..., 1010...
# one pass就可以check
class Solution(object):
    def minOperations(self, s):
        cnt1 = 0
        cnt2 = 1
        s_list = list(s)
        for i in range(len(s_list) - 1):
            if s_list[i] == s_list[i + 1]:
                cnt1 += 1
                if s_list[i] == '0':
                    s_list[i + 1] = '1'
                else:
                    s_list[i + 1] = '0'

        s_list = list(s)
        if s_list[0] == '0':
            s_list[0] = '1'
        else:
            s_list[0] = '0'

        for i in range(len(s_list) - 1):
            if s_list[i] == s_list[i + 1]:
                cnt2 += 1
                if s_list[i] == '0':
                    s_list[i + 1] = '1'
                else:
                    s_list[i + 1] = '0'
        return min(cnt1, cnt2)

test = Solution()
# print test.minOperations("0100")
# print test.minOperations("10")
# print test.minOperations("1111")
print test.minOperations("10010100")
