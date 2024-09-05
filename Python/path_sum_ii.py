# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return []

        paths = []

        def dfs(node, path):
            if not node.left and not node.right:
                if sum(path) == targetSum:
                    paths.append(path)
                    return

            if node.left:
                dfs(node.left, path + [node.left.val])

            if node.right:
                dfs(node.right, path + [node.right.val])

        dfs(root, [root.val])
        return paths
