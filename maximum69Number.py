class Solution(object):
    def maximum69Number (self, num):
        num = str(num)
        n1 = ''
        for i in range(len(num)):
            if num[i] == '6':
                n1 = num[:i] + '9' + num[i + 1:]
                break
        if n1 == '':
            return int(num)
        else:
            return int(n1)

test = Solution()
print test.maximum69Number(9669)
print test.maximum69Number(9996)
print test.maximum69Number(9999)