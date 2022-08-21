# Count the frequency of all digits in num
# Check how many pair of 9 that we have:
# If we have one pair of 9, we can make 9XXXXXX9, res = '99' now.
# If we have two pairs of 9, we can make 99XXXX99, res = '9' now.
# Continue check pairs for 8,7,6,5,4,3,2,1,0
# Strip the leading 0 in res
# Find the maximum digit left that can be used for the middle digit of palindromic number.
# final result is res + mid + reversed(res)
# For special input like 00, we need to return 0.
class Solution(object):
    def largestPalindromic(self, num):
        if num == "0" or num == "00":
            return "0"
        dic = {}
        for n in num:
            dic[n] = dic.get(n, 0) + 1
        res = ""
        for n in "9876543210":
            if n in dic:
                tmp = dic[n] / 2
                dic[n] = dic[n] % 2
                if n > 0:
                    res += n * tmp
        # Strip the leading 0
        res = res.lstrip("0")
        mid = ""
        for n in "9876543210":
            if n in dic and dic[n] == 1:
                mid = n
                break
        return res + mid + res[::-1] if res + mid + res[::-1] != "" else "0"

test = Solution()
print test.largestPalindromic("444947137")
print test.largestPalindromic("00009")