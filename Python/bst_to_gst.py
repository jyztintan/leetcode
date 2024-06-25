# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        # Keeps track of the total sum of nodes so far
        addition = 0

        # We want to perform **REVERSED** DFS In-order traversalto get the sum from higher indices to lower
        def dfs(node):
            # If empyu node, ignore
            if not node:
                return
            nonlocal addition

            # Reversed in-order traversal so DFS right side first
            dfs(node.right)

            # Process the current node value
            to_add = addition
            addition += node.val
            node.val += to_add

            # DFS left side
            dfs(node.left)

        # Initiate the Reversed in-order traversal from the root node!
        dfs(root)

        return root
