class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        special.sort()
        res = 0
        for s in special:
            res = max(res, s - bottom)
            bottom = s + 1
        res = max(res, top - bottom + 1)
        return res

    # Brutal force, TLE
    def maxConsecutive2(self, bottom, top, special):
        if bottom == top and len(special) != 0 and bottom != special[0]:
            return 1
        elif bottom == top and len(special) != 0 and bottom == special[0]:
            return 0
        elif len(special) == 0:
            return top - bottom + 1
        special.sort()
        res = 0
        cnt = 0
        for i in range(bottom, top + 1):
            if len(special) != 0 and i == special[0]:
                res = max(res, cnt)
                cnt = 0
                special.pop(0)
            else:
                cnt += 1
                res = max(res, cnt)
        return res

test = Solution()
print test.maxConsecutive(2, 9, [4,6])
print test.maxConsecutive(6, 8, [7,6,8])