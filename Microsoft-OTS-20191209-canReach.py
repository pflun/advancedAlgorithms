# -*- coding: utf-8 -*-
# You're given an array of integers, such as arr = [3,4,2,3,0,3,1,2,1], and a start index.
# When your're at an index i, you can move left or right by arr. Your task is to figure out if you can reach value 0.
# 给你一个integer array （假设可以负数），和一个startIndex,
# 写个function确认能不能到达终点，终点的值为0。
# 如果你所在位置为i, 你能move left OR right by nums [ i ].
class Solution(object):
    def canReach(self, arr, startIndex):
        if arr[startIndex] == 0:
            return True
        else:
            return self.dfs(arr, startIndex, set())

    def dfs(self, arr, index, visited):
        if index in visited:
            return
        visited.add(index)
        steps = arr[index]
        if steps == 0:
            return True
        nextPosLeft = index - steps
        nextPosRight = index + steps
        left = False
        right = False
        if nextPosLeft >= 0:
            left = self.dfs(arr, nextPosLeft, visited)
        if nextPosRight < len(arr):
            right = self.dfs(arr, nextPosRight, visited)
        return left or right

    def canReach2(self, nums, s):
        if nums[s] == 0:
            return True
        else:
            return self.helper(nums, s, {})

    def helper(self, nums, idx, dic):
        # out of boundary
        if idx < 0 or idx >= len(nums):
            return False
        steps = nums[idx]
        # found 0
        if steps == 0:
            return True
        # found in cache
        if idx in dic:
            return dic[idx]
        dic[idx] = False
        # search in left
        leftIdx = idx - steps
        rightIdx = idx + steps
        if leftIdx >= 0:
            if self.helper(nums, leftIdx, dic):
                return True
        # search in right
        if rightIdx < len(nums):
            if self.helper(nums, rightIdx, dic):
                return True
        return False

test = Solution()
print test.canReach([3,4,2,3,0,3,1,2,1], 0)
print test.canReach([3,4,2,3,0,3,1,2,1], 1)
print test.canReach([3,4,2,3,0,3,1,2,1], 2)
print test.canReach([3,4,2,3,0,3,1,2,1], 3)
print test.canReach([3,4,2,3,0,3,1,2,1], 4)
print test.canReach([2,2,2,0], 0)
print test.canReach([2,2,2,0], 1)
print test.canReach([3,4,2,3,0,3,1,2,1], 3)
print test.canReach([1,2,3,4], 3)
print '============'
print test.canReach2([3,4,2,3,0,3,1,2,1], 0)
print test.canReach2([3,4,2,3,0,3,1,2,1], 1)
print test.canReach2([3,4,2,3,0,3,1,2,1], 2)
print test.canReach2([3,4,2,3,0,3,1,2,1], 3)
print test.canReach2([3,4,2,3,0,3,1,2,1], 4)
print test.canReach2([2,2,2,0], 0)
print test.canReach2([2,2,2,0], 1)
print test.canReach2([3,4,2,3,0,3,1,2,1], 3)
print test.canReach2([1,2,3,4], 3)