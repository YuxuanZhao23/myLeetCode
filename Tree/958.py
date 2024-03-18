# Given the root of a binary tree, determine if it is a complete binary tree.

# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, 0, 1)])
        curr_depth = 0
        curr_val = 1
        while queue:
            node, depth, val = queue.popleft()
            if curr_depth == depth and curr_val == val:
                if curr_val == math.pow(2, curr_depth):
                    curr_depth += 1
                    curr_val = 1
                else:
                    curr_val += 1
            else:
                return False
            if node.left: queue.append((node.left, depth + 1, val * 2 - 1))
            if node.right: queue.append((node.right, depth + 1, val * 2))
        return True
        
            
