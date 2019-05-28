# https://www.youtube.com/watch?v=nxBMEvLqDzY
class Solution(object):
    def restoreIpAddresses(self, s):
        if len(s) < 4 or len(s) > 12:
            return []
        res = []
        # result, remaining string, current string, field/position
        self.helper(res, s, '', 0)

        return res

    def helper(self, res, s, current, field):
        # field == 4 means done
        if field == 4 and len(s) == 0:
            # remove prefix '.', because current is like '.192.168.0.1'
            res.append(current[1:])
        # not valid
        elif field == 4 or len(s) == 0:
            return
        else:
            # len(most recent field) == 1
            self.helper(res, s[1:], current + '.' + s[0], field + 1)
            # len(most recent field) == 2, .xxx.xxx.072 is not valid, remaining string exists
            if s[0] != '0' and len(s) > 1:
                self.helper(res, s[2:], current + '.' + s[:2], field + 1)
                # len(most recent field) == 3, convert that 3 digits into integer and verify if less/equal than 255
                if len(s) > 2 and int(s[0:3]) <= 255:
                    self.helper(res, s[3:], current + '.' + s[:3], field + 1)


test = Solution()
print test.restoreIpAddresses("25525511135")