# Given the root of a binary tree, return the preorder traversal of its nodes' values.
# https://leetcode.com/problems/binary-tree-preorder-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return self.dfs_approach(root)
        return self.bfs_approach(root)
    
    def dfs_approach(self, root):
        result = []
        self.dfs(root, result)
        return result
    
    def dfs(self, node, result):
        if not node: return None
        result.append(node.val)
        if node.left: self.dfs(node.left, result)
        if node.right: self.dfs(node.right, result)

    def bfs_approach(self, root):
        if not root: return []
        stack = deque()
        stack.append(root)
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return result    