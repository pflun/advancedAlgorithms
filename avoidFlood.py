from _bisect import *
class Solution(object):
    def avoidFlood(self, rains):
        cnt = 0
        res = [None for _ in range(len(rains))]
        dic = {}
        slots = []
        for i in range(len(rains)):
            if rains[i] == 0:
                cnt += 1
                slots.append(i)
            else:
                res[i] = -1
                if rains[i] in dic:
                    last = dic[rains[i]]
                    if cnt > 0:
                        # first dry day that is after the last appearance
                        found = bisect(slots, last)
                        # not available in slots
                        if found >= len(slots):
                            return []
                        else:
                            cnt -= 1
                            res[slots[found]] = rains[i]
                            del slots[found]
                            dic[rains[i]] = i
                    else:
                        return []
                else:
                    dic[rains[i]] = i
        if cnt > 0:
            for s in slots:
                res[s] = 1

        return res


test = Solution()
print test.avoidFlood([1,2,3,4])
print test.avoidFlood([1,2,0,0,2,1])
print test.avoidFlood([1,2,0,1,2])
print test.avoidFlood([69,0,0,0,69])
print test.avoidFlood([10,20,20])
print test.avoidFlood([0,1,1])