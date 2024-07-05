# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_sum = -float('inf')

    def dfs(self, root) -> int:
        if not root:
            return 0
        left = max(self.dfs(root.left), 0)
        right = max(self.dfs(root.right), 0)
        self.max_sum = max(left + root.val + right, self.max_sum)
        return root.val + max(left, right)

    def maxPathSum(self, root) -> int:
        self.dfs(root)
        return self.max_sum

