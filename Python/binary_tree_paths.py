# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root):
        ans = []
        def dfs(node, path):
            path += str(node.val)
            if not node.left and not node.right:
                ans.append(path)
                return
            path += '->'
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
            return

        dfs(root, '')
        return ans
