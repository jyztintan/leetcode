# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        inorder = []

        def dfs(node):
            if node.left:
                dfs(node.left)
            inorder.append(node)
            if node.right:
                dfs(node.right)

        dfs(root)

        idx = inorder.index(p)
        if idx == len(inorder) - 1:
            return
        return inorder[idx + 1]
