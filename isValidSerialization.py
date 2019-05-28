# https://www.youtube.com/watch?v=_mbnPPHJmTQ
# When new node add into the tree, arrow - 1 then + 2; when new # add into the tree, arrow - 1
# Init: root has 2 arrow

class Solution(object):
    def isValidSerialization(self, preorder):
        arrow = 2
        preorder = preorder.split(',')
        for char in preorder[1:]:
            if char != '#':
                arrow += 1
            else:
                arrow -= 1
                if arrow < 0:
                    return False

        return arrow == 0




test = Solution()
print test.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")