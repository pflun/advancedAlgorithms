class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []
        categorize = []
        tmp = []
        currLength = 0
        for w in words:
            if currLength + len(w) > maxWidth:
                categorize.append(tmp)
                currLength = len(w) + 1
                tmp = [w]
            else:
                currLength += len(w) + 1
                tmp.append(w)
        if len(tmp) != 0:
            categorize.append(tmp)

        for c in categorize:
            res.append(self.justify(c, maxWidth))

        return res

    def justify(self, words, maxWidth):
        spaces = len(words) - 1
        if spaces == 0:
            return words[0]
        res = ""
        empty = maxWidth - len(''.join(words))
        extra = empty % spaces
        for w in words[:-1]:
            res += w + ' ' * (empty / spaces)
            if extra > 0:
                res += ' '
                extra -= 1
        res += words[-1]
        return res

test1 = Solution()
print test1.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)