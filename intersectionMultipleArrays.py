class Solution(object):
    def intersection(self, nums):
        tmp = set()
        res = set(nums[0])
        for num in nums[1:]:
            for n in num:
                if n in res:
                    tmp.add(n)
            res = tmp
            tmp = set()
        return sorted(list(res))

test = Solution()
print test.intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]])
print test.intersection([[1,2,3],[4,5,6]])
# Solution2: the numbers in res are those appear len(nums) times, so count frequency and iterate freq_dict