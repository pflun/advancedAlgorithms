class Solution(object):
    def stringMatching(self, words):
        res = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if words[i] in words[j]:
                        res.add(words[i])

        return list(res)

test = Solution()
print test.stringMatching(["mass","as","hero","superhero"])
print test.stringMatching(["leetcode","et","code"])
print test.stringMatching(["blue","green","bu"])
print test.stringMatching(["leetcoder","leetcode","od","hamlet","am"])