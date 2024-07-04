# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def goodNodes(self, root: TreeNode) -> int:

        # Root is always a good node
        if root is None:
            return 0
        count = [1]
        def dfs(root, high):
            if root.left:
                if root.left.val >= high:
                    count[0] += 1
                dfs(root.left, max(high, root.left.val))
            if root.right:
                if root.right.val >= high:
                    count[0] += 1
                dfs(root.right, max(high, root.right.val))

        dfs(root, root.val)
        return count[0]

