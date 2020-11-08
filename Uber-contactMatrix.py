# -*- coding: utf-8 -*-
# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=683134
# contact[i][j] == 1说明 i j connected，如果i感染j也感染，initial: list of 感染的人，return 所有感染的人
# follow up: 删除一个人最终感染人数最少，return 这个人
class Solutiuon(object):
    def contactMatrix(self, contact, initial):
        self.res = set()
        self.dic = {}
        for i in range(len(contact)):
            for j in range(i + 1, len(contact[0])):
                if contact[i][j] == 1:
                    self.dic[i] = self.dic.get(i, []) + [j]
        for p in initial:
            self.helper(p)
        return list(self.res)

    def helper(self, p):
        self.res.add(p)
        if p not in self.dic:
            return
        for a in self.dic[p]:
            self.helper(a)

test = Solutiuon()
print test.contactMatrix([[1,1,1], [1,1,1], [1,1,1]], [0])