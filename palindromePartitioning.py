class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
            return []

        self.res = []

        def dfs(s, res):
            if len(s) == 0:
                self.res.append(res[:])
                return
            #
            for i in range(1, len(s) + 1):
                if self.isPalindrome(s[:i]):
                    # Backtracking
                    res.append(s[:i])
                    dfs(s[i:], res)
                    res.pop()

        dfs(s, [])
        return self.res


    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

test = Solution()
print test.partition("aab")