# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=DqhPJ8MzDKM
# DP: https://discuss.leetcode.com/topic/22948/my-dp-approach-in-python-with-comments-and-unittest
class Solution(object):
    def isMatch(self, s, p):
        # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the table with False. The first row is satisfied.
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        # empty string match empty string, '' match ''
        table[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        # * 可以代表前一位出现0次，也就是说 i位置 如果出现 * 去找 i - 2 (因为i - 1被删除)，s为空 p如果见到*依旧有可能为空
        for i in range(2, len(p) + 1):
            if p[i - 1] == '*':
                table[i][0] = table[i - 2][0]

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    # i-1 j-1位置上的字符相等或dot，从前一个对角线位置取结果
                    if p[i - 1] == s[j - 1] or p[i - 1] == '.':
                        table[i][j] = table[i - 1][j - 1]
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    table[i][j] = table[i - 2][j] or table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    # s: _b  _b
                    # p: b*  .*
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]

    # bug
    def isMatch2(self, s, p):
        def dfs(s, p, i, j):
            if i == len(s) or j == len(p):
                return False
            if i == len(s) - 1 and j == len(p) - 1 and s[i] == p[j]:
                return True
            if s[i] == p[j] or p[j] == '.':
                dfs(s, p, i + 1, j + 1)
            elif p[j] == '*' and p[j - 1] == s[i]:
                dfs(s, p, i + 1, j)
            else:
                return False

        return dfs(s, p, 0, 0)

test = Solution()
print test.isMatch("aa", "a")
print test.isMatch("aa", "a*")
print test.isMatch("ab", ".*")
print test.isMatch("aab", "c*a*b")
print test.isMatch("mississippi", "mis*is*p*.")