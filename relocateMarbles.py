class Solution(object):
    # read the question again, because only need to return occupied position (no need to memorize how many duplicates),
    # thus a set is enough, dic is not needed
    def relocateMarbles(self, nums, moveFrom, moveTo):
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        for i in range(len(moveFrom)):
            if moveFrom[i] in dic:
                curr = dic[moveFrom[i]]
                del dic[moveFrom[i]]
                dic[moveTo[i]] = dic.get(moveTo[i], 0) + curr
        res = []
        for k, v in sorted(dic.items()):
            res.append(k)
        return res

test = Solution()
print test.relocateMarbles([1,6,7,8], [1,7,2], [2,9,5])
print test.relocateMarbles([1,1,3,3], [1,3], [2,2])