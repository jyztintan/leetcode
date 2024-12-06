# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def dfs(self, root) -> int:
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.diameter = max(left + right, self.diameter)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root) -> int:
        self.dfs(root)
        return self.diameter


