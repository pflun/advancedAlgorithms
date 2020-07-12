class Solution(object):
    def shuffle(self, nums, n):
        n1 = nums[:n]
        n2 = nums[n:]
        res = []
        for i in range(n):
            res.append(n1[i])
            res.append(n2[i])
        return res

test = Solution()
print test.shuffle([2,5,1,3,4,7], 3)