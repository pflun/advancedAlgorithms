# https://www.geeksforgeeks.org/even-numbers-even-index-odd-numbers-odd-index/
class Solution(object):
    def evenOddIndex(self, arr):
        even = 0
        odd = len(arr) - 1

        while odd > 0 and even < len(arr) - 2:
            while even < len(arr) - 1:
                if arr[even] % 2 == 0:
                    even += 2
                else:
                    break
            while odd > 0:
                if arr[odd] % 2 != 0:
                    odd -= 2
                else:
                    break
            # print even, arr[even], odd, arr[odd], arr

            arr[even], arr[odd] = arr[odd], arr[even]

        return arr




test = Solution()
print test.evenOddIndex([3, 6, 12, 1, 5, 8])