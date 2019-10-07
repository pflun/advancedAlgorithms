class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        res = []
        flag = 0
        for s in source:
            s = s.strip()
            if len(s) >= 2 and s[:2] == '//':
                continue
            if len(s) >= 2 and s[:2] == '/*':
                flag = 1
            if len(s) >= 2 and s[-2:] == '*/':
                flag = 0
                continue
            if flag == 1:
                continue
            res.append(s)
        return res