class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        diff = arr[1] - arr[0]
        prev = arr[1]
        for a in arr[2:]:
            d = a - prev
            if d != diff:
                return False
            prev = a
        return True

test = Solution()
print test.canMakeArithmeticProgression([3,5,1])
print test.canMakeArithmeticProgression([1,2,4])