class Solution(object):
    def isAlienSorted(self, words, order):
        for i in range(len(words) - 1):
            if not self.isValid(words[i], words[i + 1], order):
                return False
        return True

    def isValid(self, w1, w2, order):
        i = 0
        while i < len(w1) and i < len(w2):
            if order.find(w1[i]) > order.find(w2[i]):
                return False
            elif order.find(w1[i]) < order.find(w2[i]):
                return True
            i += 1
        # case: apple vs app
        return True if i == len(w1) else False

test = Solution()
print test.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")