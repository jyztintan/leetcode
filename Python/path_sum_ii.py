# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, acc):
            if not node.left and not node.right:
                return acc == targetSum

            if node.left and dfs(node.left, acc + node.left.val):
                return True
            if node.right and dfs(node.right, acc + node.right.val):
                return True

            return False

        return dfs(root, root.val)

