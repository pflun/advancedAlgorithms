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

    # bug on apple vs app
    def isAlienSorted2(self, words, order):
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            j = 0
            while j < len(w1) and j < len(w2):
                if order.find(w1[j]) > order.find(w2[j]):
                    return False
                elif order.find(w1[j]) == order.find(w2[j]):
                    j += 1
                    continue
                else:
                    break
        return True

test = Solution()
print test.isAlienSorted2(["apple","app"], "abcdefghijklmnopqrstuvwxyz")