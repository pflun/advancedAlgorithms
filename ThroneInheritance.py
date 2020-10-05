# bug
class ThroneInheritance(object):

    def __init__(self, kingName):
        self.dead = set()
        self.family = {}
        self.root = kingName
        self.family[kingName] = []

    def birth(self, parentName, childName):
        if parentName in self.family:
            self.family[parentName].append(childName)

    def death(self, name):
        self.dead.add(name)

    def getInheritanceOrder(self):
        res = []
        self.dfs(res, self.root)
        return res

    def dfs(self, res, root):
        if root not in self.dead:
            res.append(root)
        if root in self.family:
            for child in self.family[root]:
                self.dfs(res, child)