class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        sumVal = sum(nums)
        if sumVal % k != 0:
            return False
        avg = sumVal / k

        def dfs(nums, tmp, used, i, target):
            if sum(tmp) == target:
                return tmp
            for j in range(i, len(nums)):
                if j in used:
                    continue
                tmp.append(nums[j])
                used.add(j)
                removed = dfs(nums, tmp, used, j + 1, target)
                # if found one result, exit from recursion
                if len(removed) != 0:
                    return removed
                tmp.pop()
                used.remove(j)
            # cannot find sum == target average
            return []

        while len(nums) > 0:
            removed = dfs(nums, [], set(), 0, avg)
            # cannot find sum == target average
            if len(removed) == 0:
                return False
            for v in removed:
                nums.remove(v)
        return True

test = Solution()
print test.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)