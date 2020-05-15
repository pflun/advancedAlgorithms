# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=F9bWJwzzb3E
class Solution(object):
    def isNumber(self, s):
        s = s.strip()
        met_dot = met_e = met_digit = False
        for i, char in enumerate(s):
            if char in ['+', '-']:
                # 正负号只能出现在第一个位置 或 e后面第一个位置
                if i > 0 and s[i-1] != 'e':
                    return False
            elif char == '.':
                # 遇见过 . 或 e后面不能出现小数
                if met_dot or met_e:
                    return False
                met_dot = True
            elif char == 'e':
                # 遇见过 e 或 e前面没数字（e前必须有数字）
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False
            elif char.isdigit():
                met_digit = True
            else:
                return False
        # e后面必须有数字，结合line 21，遇见e就把met_digit设为false后面检查e后是否有数字
        return met_digit