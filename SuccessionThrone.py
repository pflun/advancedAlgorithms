class TreeNode(object):
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

class SuccessionThrone(object):
    def __init__(self, firstMan):
        self.family = {}
        self.family[firstMan] = TreeNode(firstMan, firstMan)
        # ancestor
        self.firstMan = firstMan

    def birth(self, parent, name):
        if parent not in self.family:
            return -1
        else:
            self.family[parent].children.append(name)
            self.family[name] = TreeNode(name, parent)

    def death(self, name):
        if name not in self.family:
            return -1
        else:
            parent = self.family[name].parent
            children = self.family[name].children
            self.family.pop(name)
            self.family[parent].children.remove(name)
            self.family[parent].children = children + self.family[parent].children

    def getOrder(self):
        res = []
        def dfs(root, res):
            res.append(root.name)
            if len(root.children) != 0:
                for child in root.children:
                    dfs(self.family[child], res)
        dfs(self.family[self.firstMan], res)
        return res


test = SuccessionThrone(0)
test.birth(0, 1.1)
test.birth(0, 1.2)
test.birth(1.1, 2.1)
test.birth(1.1, 2.2)
print test.getOrder()