# -*- coding: utf-8 -*-
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def recoverFromPreorder(self, traversal):
        initial_split = self.exact_split(traversal, '-')
        root = TreeNode(int(initial_split[0]))
        
        if len(initial_split) == 1:
            return root
            
        left_val = initial_split[1]
        right_val = initial_split[2] if len(initial_split) == 3 else ""

        def helper(trav, depth):
            if not trav or trav == "":
                return None
            if trav.isdigit():
                return TreeNode(int(trav))

            splitter = '-' * (depth + 1)

            after_split = self.exact_split(trav, splitter)
            
            node_val = after_split[0]
            node_left_trav = None
            node_right_trav = None
            
            if len(after_split) >= 2:
                node_left_trav = after_split[1]
            if len(after_split) == 3:
                node_right_trav = after_split[2]
                
            node = TreeNode(int(node_val))
            node.left = helper(node_left_trav, depth + 1)
            node.right = helper(node_right_trav, depth + 1)
            return node

        root.left = helper(left_val, 1)
        root.right = helper(right_val, 1)

        return root

    # "1-2--3--4-5--6--7" => ['1', '2--3--4', '5--6--7']
    def exact_split(self, target_str, splitter):
        if not splitter:
            return [target_str]
            
        n = len(splitter)
        char = splitter[0]
        
        res = []
        i = 0
        last_idx = 0
        
        while i < len(target_str):
            if target_str[i] == char:
                count = 0
                start = i
                # Count consecutive characters
                while i < len(target_str) and target_str[i] == char:
                    count += 1
                    i += 1
                
                # If it matches the exact length of the splitter, cut here
                if count == n:
                    res.append(target_str[last_idx:start])
                    last_idx = i
            else:
                i += 1
                
        # Append the remaining part
        res.append(target_str[last_idx:])
        return res

# 测试代码
if __name__ == "__main__":
    sol = Solution()
    # 测试 exact_split
    print sol.exact_split("1-2--3--4-5--6--7", "-")
    
    # 测试主逻辑
    root = sol.recoverFromPreorder("1-2--3--4-5--6--7")
    print root.val
    print root.left.val
    print root.right.val
