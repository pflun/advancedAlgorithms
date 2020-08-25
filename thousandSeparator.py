class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        while n / 1000 > 0:
            remain = str(n % 1000)
            if len(remain) == 1:
                remain = '00' + remain
            elif len(remain) == 2:
                remain = '0' + remain
            res = [remain] + res
            n /= 1000
        res = [str(n % 1000)] + res
        return '.'.join(res)