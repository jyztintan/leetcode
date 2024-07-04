# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder, postorder):
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        if len(preorder) > 1:
            left = preorder[1]
            idx = postorder.index(left)
            root.left = self.constructFromPrePost(preorder[1:idx + 2], postorder[:idx + 1])
            root.right = self.constructFromPrePost(preorder[idx + 2:], postorder[idx + 1: -1])
        return root