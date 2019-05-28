class Solution(object):
    def findWords(self, words):
        upper_row = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
        mid_row = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
        lower_row = ['Z', 'X', 'C', 'V', 'B', 'N', 'M']

        upper_counter = 0
        mid_counter = 0
        lower_counter = 0

        res = []

        for word in words:
            hash_words = set(word.upper())
            for c in hash_words:
                if c in upper_row:
                    upper_counter += 1
                elif c in mid_row:
                    mid_counter += 1
                elif c in lower_row:
                    lower_counter += 1
            if upper_counter == len(hash_words) or mid_counter == len(hash_words) or lower_counter == len(hash_words):
                res.append(word)
            upper_counter = mid_counter = lower_counter = 0

        return res

test = Solution()
print test.findWords(["Hello","Alaska","Dad","Peace"])