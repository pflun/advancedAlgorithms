# -*- coding: utf-8 -*-
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/106493/C%2B%2B-O(n)-solution-two-pass
# below code bug
class Solution(object):
    def isPossible(self, nums):
        freq = {}
        tails = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for n in nums:
            if n not in freq:
                continue
            freq[n] -= 1
            if tails[n - 1] > 0:
                tails[n - 1] -= 1
                tails[n] += 1
            elif freq[n + 1] and freq[n + 2]:
                freq[n + 1] -= 1
                ferq[n + 2] -= 1
                tails[n + 2] += 1
            else:
                return False
        return True

    # https://www.cnblogs.com/grandyang/p/7525821.html
    # 两个dict，一个统计频率，另一个记录 一组连续的末尾数字 => 出现的频率，如果是新起点看后面2哥数字频率还有没有，没有就false
    def isPossible2(self, nums):
        freq = {}
        need = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for n in nums:
            if freq[n] == 0:
                continue
            # 新起点，判断后面2哥频率还有没有，有的话就从频率中减去，再need中生成一次三连
            elif n + 1 in freq and n + 2 in freq and freq[n + 1] > 0 and freq[n + 2] > 0:
                freq[n + 1] -= 1
                freq[n + 2] -= 1
                need[n + 3] = need.get(n + 3, 0) + 1
            # 连上
            elif n in need and need[n] > 0:
                need[n] -= 1
                need[n + 1] = need.get(n + 1, 0) + 1
            else:
                return False
            # 用掉当前这张牌所以从频率中减去
            freq[n] -= 1
        return True

# https://www.youtube.com/watch?v=GzEek52CyW8&t=467s
# 小Q这个状态机的解法似乎更好，贪心法优先给能接上的，不能接上重新开序列，
# 1和2还没接好（状态机里不为0就是还存在没接好，为0就是接好了进位给3）再重开序列就返回false
# 当前 len = 1的集合 1 0 0 1 0 0 0 0
#      len = 2      0 1 0 0 1 1 1 0
#      len >= 3     0 0 1 1 1 1 1 2
# [1,2,3,3,4,4,5,5] 1 2 3 3 4 4 5 5

test = Solution()
print test.isPossible2([1,2,3,3,4,4,5,5])