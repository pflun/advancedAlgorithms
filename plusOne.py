class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        if digits[0] == 0:
            digits = [1] + digits
        print digits

    def plusOne2(self, digits):
        carry, curr = divmod(digits[-1] + 1, 10)
        digits[-1] = curr
        pos = len(digits) - 2
        while carry == 1 and pos >= 0:
            carry, curr = divmod(digits[pos] + carry, 10)
            digits[pos] = curr
            pos -= 1

        if carry == 1:
            digits = [1] + digits
        return digits


test = Solution()
test.plusOne([9, 2, 2])