class Solution(object):
    def lemonadeChange(self, bills):
        dic = {}
        for b in bills:
            if b == 5:
                dic[5] = dic.get(5, 0) + 1
            elif b == 10:
                dic[10] = dic.get(10, 0) + 1
                dic[5] = dic.get(5, 0) - 1
                if dic[5] < 0:
                    return False
            elif b == 20:
                if 10 in dic and dic[10] > 0:
                    dic[10] = dic.get(10, 0) - 1
                    dic[5] = dic.get(5, 0) - 1
                else:
                    dic[5] = dic.get(5, 0) - 3
                if dic[5] < 0:
                    return False

        return True

test = Solution()
print test.lemonadeChange([5,5,10,10,20])