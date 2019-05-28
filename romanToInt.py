class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        if s == "":
            return 0

        # first compare is right-est digits
        index = len(s) - 2
        # init with right-est
        sum = ROMAN[s[-1]]
        # from s[right] to s[left]
        while index >= 0:
            # ie. IV = 5 - 1
            if ROMAN[s[index]] < ROMAN[s[index + 1]]:
                sum -= ROMAN[s[index]]
            # ie. VI = 5 + 1
            else:
                sum += ROMAN[s[index]]
            index -= 1
        return sum

test = Solution()
print test.romanToInt("XLV")