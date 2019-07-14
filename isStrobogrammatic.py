class Solution(object):
    def isStrobogrammatic(self, num):
        dic = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        res = ''
        for n in num:
            if n not in dic:
                return False
            else:
                res = dic[n] + res
        return True if res == num else False

test = Solution()
print test.isStrobogrammatic('69')
print test.isStrobogrammatic('818')