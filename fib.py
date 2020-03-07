class Solution(object):
    def fib(self, N):
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            prev = 0
            curr = 1
            for _ in range(N - 1):
                tmp = prev + curr
                prev = curr
                curr = tmp
            return curr