class Solution(object):
    def reformatNumber(self, number):
        number = "".join(number.split())
        number = number.replace('-','')
        res = []
        while len(number) > 4:
            curr = number[:3]
            res.append(curr)
            number = number[3:]
        if len(number) == 2:
            res.append(number)
        elif len(number) == 3:
            res.append(number)
        else:
            res.append(number[:2])
            res.append(number[2:])
        return '-'.join(res)

test = Solution()
print test.reformatNumber("1-23-45 6")
print test.reformatNumber("123 4-567")
print test.reformatNumber("123 4-5678")
print test.reformatNumber("12")
print test.reformatNumber("--17-5 229 35-39475 ")