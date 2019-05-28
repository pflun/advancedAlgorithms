class Solution(object):
    def letterCombinations(self, digits):
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = ['']

        for digit in digits:
            # get abc
            chars = dic[digit]
            newresult = []
            # for a, b, c
            for char in chars:
                # take prev res (ie. ['ad', 'bd', 'cd']), add new char for each prev string
                for str in res:
                    newresult.append(str + char)
            # Update res
            res = newresult

        return res

    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.res = []
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def dfs(digits, tmp, index):
            if len(tmp) == len(digits):
                self.res.append(''.join(tmp[:]))
                return

            curr = dic[digits[index]]
            for char in curr:
                tmp.append(char)
                dfs(digits, tmp, index + 1)
                tmp.pop()

        dfs(digits, [], 0)

        return self.res

test = Solution()
print test.letterCombinations2('23')