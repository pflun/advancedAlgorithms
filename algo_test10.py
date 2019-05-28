class Solution(object):
    def __init__(self):
        self.val = 10

    def test(self):
        return self.val

class Solution2(object):
    def getS1(self):
        # s = set()
        # s.add((1, 2))
        # if (1, 2) not in s:
        #     print 'yes'
        # else:
        #     s.remove((1, 2))
        #     print len(s)
        return Solution().test()

test = Solution2()
print test.getS1()

class Solution3(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(s) == 0 or len(wordDict) == 0:
            return False

        self.mem = {}

        def helper(s, wordDict):
            if s in self.mem:
                if self.mem[s]:
                    return True
                else:
                    return False
            if s in wordDict:
                self.mem[s] = True
                return True
            else:
                self.mem[s] = False

            for i in range(1, len(s)):
                left = helper(s[:i], wordDict)
                right = helper(s[i:], wordDict)
                if left and right:
                    return True
            return False

        return helper(s, wordDict)

test2 = Solution3()
print test2.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])

class Solution4(object):
    def tonggou(self, s1, s2):
        dic1 = {}
        dic2 = {}
        l1 = []
        l2 = []
        for s in s1:
            dic1[s] = dic1.get(s, 0) + 1
        for s in s2:
            dic2[s] = dic2.get(s, 0) + 1

        for key, val in dic1.items():
            l1.append(val)
        for key, val in dic2.items():
            l2.append(val)

        return sorted(l1) == sorted(l2)

test3 = Solution4()
print test3.tonggou('pllsslo', 'addqqdy')

print ord('a')