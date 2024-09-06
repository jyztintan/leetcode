# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)
class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []

        order = []

        def dfs(node):
            order.append(node)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)
        curr = root
        for node in order[1:]:
            curr.left = None
            curr.right = node
            curr = node

        return root

# # Nodes creation
# node1 = TreeNode(1)
# node2 = TreeNode(2)
# node5 = TreeNode(5)
# node3 = TreeNode(3)
# node4 = TreeNode(4)
# node6 = TreeNode(6)
#
# # Establishing the connections
# node1.left = node2
# node1.right = node5
# node2.left = node3
# node2.right = node4
# node5.right = node6
#
# # The root of the tree
# root = node1
# print(Solution().flatten(root))
