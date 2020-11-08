class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        res = []
        for i in range(len(l)):
            curr = nums[l[i]:r[i] + 1]
            if len(curr) == 1:
                res.append(True)
                continue
            s1, s2 = self.findSmalls(curr)
            hashSet = set(curr)
            diff = s2 - s1
            if diff == 0:
                if len(hashSet) != 1:
                    res.append(False)
                    continue
                else:
                    res.append(True)
                    continue
            else:
                for _ in range(len(curr) - 2):
                    s2 += diff
                    if s2 not in hashSet:
                        res.append(False)
                        break
                if len(res) == i + 1:
                    continue
                else:
                    res.append(True)

        return res

    def findSmalls(self, curr):
        s1 = min(curr[0], curr[1])
        s2 = max(curr[0], curr[1])
        for a in curr[2:]:
            if a < s1:
                s2 = s1
                s1 = a
            elif a < s2:
                s2 = a
        return s1, s2

test = Solution()
print test.checkArithmeticSubarrays([4,6,5,9,3,7], [0,0,2], [2,3,5])
# print test.checkArithmeticSubarrays([-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], [0,1,6,4,8,7], [4,4,9,7,9,10])