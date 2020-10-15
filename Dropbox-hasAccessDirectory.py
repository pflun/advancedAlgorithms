# -*- coding: utf-8 -*-
# https://paper.dropbox.com/doc/Dropbox-NM0Ap7llxjNJW3G7oQAV8
# Given a list folders        vector of pairs
# folders = { {“A”,” “} , {“B”,”A”}, {“C”,”A”}. {“D”, “C”}, {“E”,”C”}… } (child, parent)
# and given an access list of folders
# access  =     {“B”, ”D”}
#
# implement a API         bool   hasAccess (string name)
# for example       hasAccess (“A”) ==  True       hasAccess (“B”)  == false
# /A
# |___ /B
#     |___ /C <-- access
#     |___ /D
# |___ /E <-- access
#     |___ /F
#         |___ /G
# folders = [
#     ('A', None),
#     ('B', 'A'),
#     ('C', 'B'),
#     ('D', 'B'),
#     ('E', 'A'),
#     ('F', 'E'),
# ]
# access = set(['C', 'E'])
# has_access("B") -> false
# has_access("C") -> true
# has_access("F") -> true
# has_access("G") -> true
class Solution(object):
    def __init__(self, folders, access):
        self.childParent = {}
        self.access = access
        # for follow up
        self.parentChild = {}
        for f in folders:
            # child => parent
            self.childParent[f[0]] = f[1]
            self.parentChild[f[1]] = self.parentChild.get(f[1]) + [f[0]]

    def hasAccess(self, folder):
        if not folder:
            return False
        elif folder in self.access:
            return True
        res = self.hasAccess(self.childParent[folder])
        if res:
            self.access.add(folder)
        return res

    # followup返回可以访问的所有文件
    def allAccess(self):
        res = set()
        def helper(folder):
            if folder not in self.parentChild:
                return
            for f in self.parentChild[folder]:
                res.add(f)
                helper(f)

        for a in self.access:
            helper(a)
        return res

test = Solution([['A', ''], ['B', 'A'], ['C', 'A'], ['D', 'C'], ['E', 'C']], set(['C', 'E']))
print test.hasAccess('B')
print test.hasAccess('C')
