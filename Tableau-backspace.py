# 1 byte "0xxxxxxx"
# 2 bytes "1xxxxxxx0/1xxxxxxx"
# input: list of strings, start index of target character, output: backspace how many bytes
# ["0xxxxxxx", "1xxxxxxx", "1xxxxxxx"] backspace 2 bytes
class Solution(object):
    def backspace(self, arr, targetIdx):
        if len(arr[:targetIdx]) > 2:
            i = len(arr[:targetIdx - 2])
            while i >= 0:
                if arr[i][0] == "0":
                    break
                i -= 1
        if targetIdx - i / 2 == 0:
            return 2
        else:
            return 1
        # edge case len(arr[:targetIdx]) <= 2