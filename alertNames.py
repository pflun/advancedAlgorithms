class Solution(object):
    def alertNames(self, keyName, keyTime):
        dic = {}
        for i in range(len(keyName)):
            dic[keyName[i]] = dic.get(keyName[i], []) + [keyTime[i]]
        res = []
        for k, v in dic.items():
            if self.helper(v):
                res.append(k)
        res.sort()
        return res

    def helper(self, times):
        if len(times) < 3:
            return False
        times.sort()
        for i in range(len(times) - 2):
            first = times[i]
            last = times[i + 2]
            first = sum(x * int(t) for x, t in zip([60, 1], first.split(":")))
            last = sum(x * int(t) for x, t in zip([60, 1], last.split(":")))
            if last > first and  last - first <= 60:
                return True
        return False

test = Solution()
print test.alertNames(["daniel","daniel","daniel","luis","luis","luis","luis"], ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"])
# print test.helper(["10:00","10:40","11:00"])
# print test.helper(["09:00","11:00","13:00","15:00"])
print test.alertNames(["alice","alice","alice","bob","bob","bob","bob"], ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"])
print test.alertNames(["john","john","john"], ["23:58","23:59","00:01"])
print test.alertNames(["leslie","leslie","leslie","clare","clare","clare","clare"], ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"])