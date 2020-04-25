# https://www.geeksforgeeks.org/sum-two-large-numbers/
# two float numbers
class Solution(object):
    def sumTwoNumbers(self, str1, str2):
        n1, f1 = str1.split('.')[0], str1.split('.')[1]
        n2, f2 = str2.split('.')[0], str2.split('.')[1]
        carry = 0
        resf = ''
        i = min(len(f1), len(f2)) - 1
        while i >= 0:
            v1 = int(f1[i])
            v2 = int(f2[i])
            carry, curr = divmod(v1+v2+carry, 10)
            resf = str(curr) + resf
            i -= 1
        if len(f1) > len(f2):
            resf = resf + "".join(f1[len(f2):])
        elif len(f1) < len(f2):
            resf = resf + "".join(f2[len(f1):])
        resn = ''
        i = 0
        n1 = n1[::-1]
        n2 = n2[::-1]
        while i < max(len(n1), len(n2)):
            if i >= len(n1):
                v1 = 0
            else:
                v1 = int(n1[i])
            if i >= len(n2):
                v2 = 0
            else:
                v2 = int(n2[i])
            carry, curr = divmod(v1+v2+carry, 10)
            resn = str(curr) + resn
            i += 1
        if carry == 1:
            return '1' + resn + '.' + resf
        else:
            return resn + '.' + resf

test = Solution()
print test.sumTwoNumbers('123.456', '234.56')