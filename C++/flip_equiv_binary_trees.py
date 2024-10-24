# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipEquiv(self, root1, root2) -> bool:
        # If one of the sub-tree roots do not exist, both roots shouldn't exist
        if not (root1 and root2):
            return not root1 and not root2

        # If root don't match
        if root1.val != root2.val:
            return False

        # Check for matching left sub-tree
        if not (self.flipEquiv(root1.left, root2.left) or self.flipEquiv(root1.left, root2.right)):
            return False

        # Check for matching right sub-tree
        if not (self.flipEquiv(root1.right, root2.right) or self.flipEquiv(root1.right, root2.left)):
            return False

        return True