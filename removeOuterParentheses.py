class Solution(object):
    def removeOuterParentheses(self, S):
        res = []
        cnt = 0
        tmp = ''
        for s in S:
            if s == '(':
                cnt += 1
            elif s == ')':
                cnt -= 1
            tmp += s
            if cnt == 0 and len(tmp) != 0:
                res.append(tmp)
                cnt = 0
                tmp = ''
        rnt = []
        for r in res:
            rnt.append(r[1:-1])
        return "".join(rnt)