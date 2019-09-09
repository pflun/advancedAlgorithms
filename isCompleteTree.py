class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# bug on case: [1,2,3,4,5,null,7], BFS is actually simpler
class Solution(object):
    def isCompleteTree(self, root):
        self.level = 0
        self.flag = False

        def dfs(root, lvl):
            if not root:
                return True
            if not root.left and not root.right:
                if self.level == 0:
                    self.level = lvl
                    return True
                else:
                    if self.flag == False:
                        if self.level == lvl:
                            return True
                        elif self.level == lvl + 1:
                            self.flag = True
                            return True
                        else:
                            return False
                    else:
                        if self.level != lvl:
                            return False
                        else:
                            return True
            return dfs(root.left, lvl + 1) and dfs(root.right, lvl + 1)

        return dfs(root, 0)