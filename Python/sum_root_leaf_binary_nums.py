# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = [0]

        def dfs(node, curr):
            curr <<= 1
            curr += node.val
            if not node.right and not node.left:
                total[0] += curr
            if node.left:
                dfs(node.left, curr)
            if node.right:
                dfs(node.right, curr)

        dfs(root, 0)
        return total[0]
