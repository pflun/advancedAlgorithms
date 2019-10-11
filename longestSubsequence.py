class Solution(object):
    def longestSubsequence(self, arr, difference):
        if len(arr) == 0:
            return 0
        self.res = 1
        for i in range(len(arr)):
            self.search(arr[i + 1:], arr[i] + difference, difference, 1)
        return self.res

    def search(self, subArr, target, difference, length):
        if len(subArr) <= 0:
            return
        for i in range(len(subArr)):
            if subArr[i] == target:
                self.res = max(self.res, length + 1)
                self.search(subArr[i + 1:], target + difference, difference, length + 1)

test = Solution()
print test.longestSubsequence([1,5,7,8,5,3,4,2,1], -2)
print test.longestSubsequence([1,2,3,4], 1)
print test.longestSubsequence([1,3,5,7], 1)