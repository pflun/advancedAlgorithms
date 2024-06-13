# https://leetcode.com/problems/k-th-symbol-in-grammar/solutions/365364/java-easy-to-understand-recursion/
class Solution(object):
    def kthGrammar(self, n, k):
        if n == 1:
            return 0
        if k % 2 == 0:
            if self.kthGrammar(n - 1, k / 2) == 0:
                return 1
            else:
                return 0
        else:
            if self.kthGrammar(n - 1, (k + 1) / 2) == 0:
                return 0
            else:
                return 1

# think of the problem like this
#           0
#       /       \
#      0          1
#    /   \      /    \
#    0     1    1      0
#  / \     / \   / \   / \
#  0  1   1   0  1  0  0  1
