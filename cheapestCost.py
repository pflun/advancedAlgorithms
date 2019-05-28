# -*- coding: utf-8 -*-
# The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary). The root is the company itself, and every node in the tree represents a car distributor that receives cars from the parent node and ships them to its children nodes. The leaf nodes are car dealerships that sell cars direct to consumers. In addition, every node holds an integer that is the cost of shipping a car to it.
# A path from Honda’s factory to a car dealership, which is a path from the root to a leaf in the tree, is called a Sales Path. The cost of a Sales Path is the sum of the costs for every node in the path. For example, in the tree above one Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).
# Honda wishes to find the minimal Sales Path cost in its distribution tree. Given a node rootNode, write an function getCheapestCost that calculates the minimal Sales Path cost in the tree.
# Implement your function in the most efficient manner and analyze its time and space complexities.

# Tip: define global var, need 2 global res
# def f1():
#     global res
#     res = []
# def f2():
#     global res
#     res.append(something)

def get_cheapest_cost(rootNode):
    if not rootNode:
        return 0

    global res
    res = float('inf')

    helper(rootNode, 0)

    return res

def helper(root, tmp):
    if not root:
        return None
    tmp += root.cost

    if len(root.children) == 0:
        global res
        res = min(res, tmp)

    for child in root.children:
        helper(child, tmp)


##########################################
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node
class Node:
    # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None

head_node = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
head_node.children.append(n1)
head_node.children.append(n2)
n2.children.append(n3)
n4.children.append(n4)

print get_cheapest_cost(head_node)