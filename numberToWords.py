# -*- coding: utf-8 -*-
# 从个位往大处理，每次处理三位
# helper处理具体三位的文字，while负责加'空'／千／百万／十亿
# while每次除以1000然后交给下次循环，words每次append上次得到的文字
class Solution(object):
    def __init__(self):
        self.LESS_THAN_20 = ["", "One", "Two", "Three", "Four",
                        "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                        "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                        "Eighteen", "Nineteen"]
        self.TENS = ["", "Ten", "Twenty", "Thirty", "Forty",
                "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.THOUSANDS = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):

        if num == 0:
            return "Zero"

        words = ""
        i = 0
        while num > 0:
            # 若千位以下有值
            if num % 1000 != 0:
                # append(空／Thousand/Million/Billion) after 千位以下的数字，然后再除以1000给下次循环
                words = self.helper(num % 1000) + self.THOUSANDS[i] + " " + words
                print words
            num /= 1000
            i += 1

        # remove tail space
        return words.strip(' ')

    # Return words less than 1000, ie: One Hundred Twenty Three
    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.LESS_THAN_20[num] + " "
        elif num < 100:
            return self.TENS[num / 10] + " " + self.helper(num % 10)
        else:
            # 100 ~ 999
            return self.LESS_THAN_20[num / 100] + " Hundred " + self.helper(num % 100)


test = Solution()
print test.numberToWords(1234567)