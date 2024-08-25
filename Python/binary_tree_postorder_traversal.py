# Definition for a binary tree node.
import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root):
        ans = []

        def dfs(node):
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            ans.append(node.val)

        dfs(root)
        return ans
        # q = queue.Queue()
        # q.put(root)
        # visited = set()
        # while not q.empty():
        #     node = q.get()
        #     visited.add(node)
        #     if node.left:
        #         q.put(node.left)
        #     if node.right:
        #         q.put(node.right)


