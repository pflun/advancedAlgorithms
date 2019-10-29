class Solution(object):
    def validPhoneNumber(self, file):
        res = []
        for n in file:
            if self.isValid(n):
                res.append(n)
        return res

    def isValid(self, n):
        # xxx-xxx-xxxx
        c1 = n.split('-')
        if len(c1) == 3:
            s1 = [c for c in c1[0] if c.isdigit()]
            s2 = [c for c in c1[1] if c.isdigit()]
            s3 = [c for c in c1[2] if c.isdigit()]
            if len(s1) == 3 and len(s2) == 3 and len(s3) == 4:
                return True

        # (xxx) xxx-xxxx
        c2 = n.split(' ')
        if len(c2) == 2:
            c21 = c2[0]
            c3 = c2[1].split('-')
            if len(c3) == 2:
                c22 = c3[0]
                c23 = c3[1]
                if c21[0] == '(' and c21[-1] == ')':
                    c21 = c21[1:-1]
                    s1 = [c for c in c21 if c.isdigit()]
                    s2 = [c for c in c22 if c.isdigit()]
                    s3 = [c for c in c23 if c.isdigit()]
                    if len(s1) == 3 and len(s2) == 3 and len(s3) == 4:
                        return True
        return False

test = Solution()
print test.validPhoneNumber(['987-123-4567', '123 456 7890', '(123) 456-7890'])