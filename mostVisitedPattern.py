# DoorDash
class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        dic = {}
        for i in range(len(username)):
            dic[username[i]] = dic.get(username[i], []) + [[timestamp[i], website[i]]]
        cnt = {}
        res = ''
        for v in dic.values():
            v.sort()
            for i in range(len(v)):
                for j in range(i + 1, len(v)):
                    for k in range(j + 1, len(v)):
                        tmp = v[i][1] + '_' + v[j][1] + '_' + v[k][1]
                        cnt[tmp] = cnt.get(tmp, 0) + 1

                        # ensure lexi order
                        if res == '' or cnt[res] < cnt[tmp]:
                            res = tmp
        return res.split('_')

test = Solution()
print test.mostVisitedPattern(["joe","joe","joe","james","james","james","james","mary","mary","mary"], [1,2,3,4,5,6,7,8,9,10],
                              ["home","about","career","home","cart","maps","home","home","about","career"])