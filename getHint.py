# ACC
class Solution(object):
    def getHint(self, secret, guess):
        if not secret or not guess:
            return
        dic = {}
        A = 0
        B = 0
        p = 0

        # find how many As
        while p < len(secret) and p < len(guess):
            if secret[p] == guess[p]:
                A += 1
            p += 1

        # stat numbers for secret
        for char in secret:
            dic[char] = dic.get(char, 0) + 1

        # find how many commons totally (including B and A)
        for char in guess:
            # if dic[char] < 0, no common between secret and guess
            if char in dic and dic[char] > 0:
                B += 1
                dic[char] = dic.get(char) - 1

        # if A has value (not 0), B = total commons - A
        B -= A
        res = str(A) + 'A' + str(B) + 'B'

        return res

test = Solution()
print test.getHint("1807", "7810")