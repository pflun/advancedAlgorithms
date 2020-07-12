class Solution(object):
    def arrangeWords(self, text):
        if len(text) == 0:
            return ''
        res = ''
        dic = {}
        tests = text.split(" ")
        for t in tests:
            dic[len(t)] = dic.get(len(t), []) + [t.lower()]
        for k, v in sorted(dic.items()):
            for w in v:
                res += w + ' '
        return res[:-1].capitalize()

test = Solution()
print test.arrangeWords("Leetcode is cool")
print test.arrangeWords("Keep calm and code on")
print test.arrangeWords("To be or not to be")