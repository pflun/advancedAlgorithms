# -*- coding: utf-8 -*-
# 输入是"<html><head><body>content</body></head></html>"
class TreeNode(object):
    def __init__(self, tag, text):
        self.tag = tag
        self.text = text
        self.children = []

class Solution(object):
    def deserialize(self, data):
        return self.helper(data)

    def helper(self, data):
        if len(data) == 0:
            return
        tagName = data[data.find('<') + 1:data.find('>')]
        data = data[data.find('>') + 1:]
        secondIdx = data.find('</' + tagName)
        childrenStr = data[:secondIdx]
        children = []
        while len(childrenStr) > 0:
            childName = childrenStr[childrenStr.find('<') + 1:childrenStr.find('>')]
            childSecondIdx = childrenStr.find('</' + childName)
            childrenStr = childrenStr[childrenStr.find('>') + 1:]
            childNode = self.helper(childrenStr[:childSecondIdx])
            children.append(childNode)
            childrenStr = childrenStr[childSecondIdx:]
        node = TreeNode(tagName, '')
        node.children = children
        return node


test = Solution()
print test.deserialize('<html><head><body>content</body></head></html>')