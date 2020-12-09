class Solution(object):
    def canFormArray(self, arr, pieces):
        dic = {}
        for p in pieces:
            dic[p[0]] = p
        res = []
        for a in arr:
            res += dic.get(a, [])
        return True if res == arr else False