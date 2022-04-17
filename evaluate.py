class Solution(object):
    def evaluate(self, s, knowledge):
        dic = {}
        for k in knowledge:
            dic[k[0]] = k[1]
        res = ''
        left = -1
        right = 0
        while right < len(s):
            if s[right] == '(':
                left = right + 1
            elif s[right] == ')':
                curr = s[left:right]
                if curr in dic:
                    res += dic[curr]
                else:
                    res += '?'
                left = -1
            else:
                if left == -1:
                    res += s[right]
            right += 1
        return res

test = Solution()
print test.evaluate("(name)is(age)yearsold", [["name","bob"],["age","two"]])
print test.evaluate("hi(name)", [["a","b"]])
print test.evaluate("(a)(a)(a)aaa", [["a","yes"]])
print test.evaluate("(a)(b)", [["a","b"],["b","a"]])