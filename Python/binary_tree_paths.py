# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        curr = []

        def dfs(node):
            curr.append(str(node.val))
            if not node.left and not node.right:
                s = "->".join(curr)
                paths.append(s)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

            curr.pop()

        dfs(root)
        return paths

