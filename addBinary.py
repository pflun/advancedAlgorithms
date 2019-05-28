class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) == 0: return b
        if len(b) == 0: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1], b[0:-1]) + '0'
        else:
            return self.addBinary(a[0:-1], b[0:-1]) + '1'

    def addBinary2(self, a, b):
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        carry = 0
        res = ''
        while a or b:
            if a:
                # get last digit
                v1 = int(a[-1])
                # delete last digit, 1111 -> 111
                a = a[:-1]
            else:
                v1 = 0
            if b:
                v2 = int(b[-1])
                b = b[:-1]
            else:
                v2 = 0
            # mod 2
            carry, val = divmod(v1 + v2 + carry, 2)
            res = res + str(val)

        if carry == 1:
            res = res + str(carry)

        # Reverse string
        return "".join(reversed(res))


test = Solution()
print test.addBinary2("111", "1001")