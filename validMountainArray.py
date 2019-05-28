def validMountainArray(self, A):
    i, j, n = 0, len(A) - 1, len(A)
    while i + 1 < n and A[i] < A[i + 1]: i += 1
    while j > 0 and A[j - 1] > A[j]: j -= 1
    return 0 < i == j < n - 1