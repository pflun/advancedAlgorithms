class Solution(object):
    def nextBeautifulNumber(self, n):
        for i in range(n + 1, 1224445):
            dic = {}
            for j in str(i):
                dic[j] = dic.get(j, 0) + 1
            if all(int(k) == v for k, v in dic.items()):
                return i

    # Binary Search
    def nextBeautifulNumber2(self, n):
        # first element strictly greater A[i] > x, return index
        def upper_bound(arr, x):
            l = 0
            r = len(arr)
            while l < r:
                m = (l + r) / 2
                if arr[m] > x:
                    r = m
                else:
                    l = m + 1
            return l

        # Improvement: backtracking to generate all valid numbers
        def precompute():
            balance = []
            for i in range(1224445):
                dic = {}
                for j in str(i):
                    dic[j] = dic.get(j, 0) + 1
                if all(int(k) == v for k, v in dic.items()):
                    balance.append(i)
            return balance

        candidates = precompute()
        return candidates[upper_bound(candidates, n)]

test = Solution()
print test.nextBeautifulNumber2(3000)
print test.nextBeautifulNumber2(748601)