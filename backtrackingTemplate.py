# backtracking find combination equals to target, [1,2,2,3], target = 3 then return [1, 2]
# remove if len(removed) != 0, append to self.res when found, this will return all results (instead of one)
class Solution(object):
    def dfstest(self, nums, tmp, used, i, target):
        if sum(tmp) == target:
            return tmp
        for j in range(i, len(nums)):
            if j in used:
                continue
            tmp.append(nums[j])
            used.add(j)
            removed = self.dfstest(nums, tmp, used, j + 1, target)
            # if found one result, exit from recursion
            if len(removed) != 0:
                return removed
            tmp.pop()
            used.remove(j)
        # cannot find sum == target average
        return []

test = Solution()
print test.dfstest([1,2,2,3], [], set(), 0, 3)