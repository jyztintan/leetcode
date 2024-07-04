# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:

        count = [0]
        val = [-1]
        def in_order(node):
            if not node:
                return
            in_order(node.left)
            count[0] += 1
            if count[0] == k:
                val[0] = node.val
            in_order(node.right)

        in_order(root)
        return val[0]
