class Solution(object):
    def maximumTime(self, time):
        res = ""
        for i in range(len(time) - 1, -1, -1):
            if time[i] == ":":
                res = ":" + res
            elif time[i] == "?":
                if i == 4:
                    res = '9' + res
                elif i == 3:
                    res = '5' + res
                elif i == 1 and time[:2] == "??":
                    res = '23' + res
                    break
                elif i == 1:
                    if time[0] == '2':
                        res = '3' + res
                    else:
                        res = '9' + res
                elif i == 0:
                    if int(res[0]) > 3:
                        res = '1' + res
                    else:
                        res = '2' + res

            else:
                res = time[i] + res
        return res

test = Solution()
# print test.maximumTime("2?:?0")
# print test.maximumTime("0?:3?")
# print test.maximumTime("1?:22")
# print test.maximumTime("?4:03")
print test.maximumTime("?0:15")