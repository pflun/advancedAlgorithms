class Solution(object):
    def mergeThreeSortedArray(self, A, B, C):
        i = j = k = 0
        prev = float('-inf')
        res = []
        # each time only append smallest value, completed array mark as infinity
        while i < len(A) or j < len(B) or k < len(C):
            a = A[i] if i < len(A) else float('inf')
            b = B[j] if j < len(B) else float('inf')
            c = C[k] if k < len(C) else float('inf')
            minVal = min([a, b, c])
            res.append(minVal)
            prev = min(prev, minVal)
            if a == minVal:
                i += 1
            if b == minVal:
                j += 1
            if c == minVal:
                k += 1
        return res

test = Solution()
print test.mergeThreeSortedArray([1, 2, 3], [2, 4], [1, 4, 5])