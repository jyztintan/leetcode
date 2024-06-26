# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        nodes = []
        def dfs(node):
            # If empty node, ignore
            if not node:
                return

            # In-order traversal so DFS left side first
            dfs(node.left)

            # Process the current node value
            nodes.append(node)

            # DFS right side
            dfs(node.right)

        # Get the sorted nodes
        dfs(root)

        def construct_bst(nodes):
            if not nodes:
                return None

            # Always set the middle element to be the root so that it is guaranteed to be balanced
            mid = len(nodes) // 2
            root = nodes[mid]
            root.left = construct_bst(nodes[:mid])
            root.right = construct_bst(nodes[mid+1:])
            return root

        # Construct a new BST which is guaranteed to be balanced
        return construct_bst(nodes)

