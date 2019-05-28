class Solution:
    # @param {string} num1 a non-negative integers
    # @param {string} num2 a non-negative integers
    # @return {string} return sum of num1 and num2
    def addStrings(self, num1, num2):
        num1 = int(num1)
        num2 = int(num2)

        return str(num1 + num2)

    def addStrings2(self, num1, num2):
        tens = 1
        number1 = 0
        for i in reversed(num1):
            number1 += int(i) * tens
            tens *= 10
        tens = 1
        number2 = 0
        for j in reversed(num2):
            number2 += int(j) * tens
            tens *= 10

        return str(number1 + number2)

test = Solution()
print test.addStrings2("123", "45")