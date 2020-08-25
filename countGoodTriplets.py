class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        res = 0
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        res += 1
        return res

test = Solution()
print test.countGoodTriplets([3,0,1,1,9,7], 7, 2, 3)
print test.countGoodTriplets([1,1,2,2,3], 0, 0, 1)