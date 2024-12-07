# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]

        def dfs(node, limit):
            if not node:
                return

            if node.val >= limit:
                count[0] += 1

            limit = max(limit, node.val)
            dfs(node.left, limit)
            dfs(node.right, limit)

        dfs(root, -float('inf'))
        return count[0]
