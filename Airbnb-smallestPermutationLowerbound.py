# -*- coding: utf-8 -*-
# 给一个无序的integer,比如4139, 和一个lower bound 比如 200, 找出smallest permutation of 4319 that is greater or equal to 200
# 如果 is_greater = True：说明我们前面填的数字已经比 bound 大了，当前这一位绝对自由，闭着眼睛选剩下能用的最小数字即可。
# 如果 is_greater = False：说明前面填的数字和 bound 一模一样，当前这一位受到约束，只能选 > bound 对应位置的数字。
class Solution(object):
    def smallestPermutationLowerbound(self, num, bound):
        digits = str(num)
        bound_str = str(bound)
        bound_str = bound_str.zfill(len(digits))
        digits = sorted(digits)
        visited = set()

        def dfs(index, is_greater, path):
            if index == len(digits):
                return int("".join(path))
            for i in range(len(digits)):
                if i in visited:
                    continue

                # 2. 去重剪枝：如果当前字符和前一个相同，且前一个没被用过（说明是在同一个分支层级），跳过
                if i > 0 and digits[i] == digits[i-1] and (i-1) not in visited:
                    continue

                # 3. 避免首位是 0 (除非数字本来就只有 1 位)
                if index == 0 and digits[i] == '0' and len(digits) > 1:
                    continue

                # 4. 核心逻辑：前面已经更大，或者当前位 >= 限制位
                if is_greater or digits[i] >= bound_str[index]:
                    visited.add(i)
                    path.append(digits[i])

                    # 状态转移
                    next_is_greater = is_greater or (digits[i] > bound_str[index])

                    res = dfs(index + 1, next_is_greater, path)

                    # 找到了直接一路返回
                    if res != -1:
                        return res

                    # 撤销选择 (Backtrack)
                    path.pop()
                    visited.remove(i)

            return -1

        return dfs(0, False, [])