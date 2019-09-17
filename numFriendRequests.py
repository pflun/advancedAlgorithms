# https://leetcode.com/problems/friends-of-appropriate-ages/discuss/127029/C%2B%2BJavaPython-Easy-and-Straight-Forward
# For each age a and each age b != a, if request(a, b), we will make count[a] * count[b] requests.
# For each age a, if request(a, a), we will make count[a] * (count[a] - 1) requests.
class Solution(object):
    def numFriendRequests(self, ages):
        res = 0
        dic = {}
        for a in ages:
            dic[a] = dic.get(a, 0) + 1

        for a in dic.keys():
            for b in dic.keys():
                if self.request(a, b):
                    if a != b:
                        res += dic[a] * dic[b]
                    else:
                        res += dic[a] * (dic[a] - 1)
        return res

    def request(self, a, b):
        if b <= 0.5 * a + 7 or b > a or b > 100 and a < 100:
            return False
        return True

test = Solution()
print test.numFriendRequests([20,30,100,110,120])