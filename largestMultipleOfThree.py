class Solution(object):
    def largestMultipleOfThree(self, digits):
        self.res = []
        self.used = [False] * len(digits)
        self.rnt = 0

        def dfs(digits, tmp, tmpVal, idx):
            if tmpVal % 3 == 0:
                if len(self.res) == 0 or len(tmp) > len(self.res[0]):
                    self.res = [tmp[:]]
                elif len(tmp) == len(self.res[0]):
                    self.res.append(tmp[:])

            for i in range(idx, len(digits)):
                if self.used[i]:
                    continue
                self.used[i] = True
                tmp.append(digits[i])
                tmpVal += digits[i]
                dfs(digits, tmp, tmpVal, i + 1)
                tmpVal -= digits[i]
                self.used[i] = False
                tmp.pop()

        dfs(digits, [], 0, 0)

        if len(self.res) == 0 or len(self.res[0]) == 0:
            return ''

        # 179 largest number
        for nums in self.res:
            for i in xrange(len(nums), 0, -1):
                for j in xrange(i - 1):
                    if not self.compare(nums[j], nums[j + 1]):
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
            self.rnt = max(self.rnt, self.canct(nums))

        if self.rnt == 0:
            return ''
        return str(self.rnt)

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)

    def canct(self, nums):
        res = 0
        offset = 1
        for i in range(len(nums) - 1, -1, -1):
            res += offset * nums[i]
            offset *= 10
        return res

test = Solution()
print test.largestMultipleOfThree([8,1,9])
print test.largestMultipleOfThree([8,6,1,7,0])
print test.largestMultipleOfThree([8,6,7,1,0])
print test.largestMultipleOfThree([1])
print test.largestMultipleOfThree([0,0,0,0,0,0])