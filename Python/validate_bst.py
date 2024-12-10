# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) Time/Space where N is the number of nodes.
# O(N) time as we visit each node exactly once, O(N) space as we keep the entire tree
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, lower, upper):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            return check(node.left, lower, node.val) and check(node.right, node.val, upper)

        return check(root, -float('inf'), float('inf'))


# O(N) Time/Space where N is the number of nodes.
# O(N) time as we visit each node exactly once, O(N) space as we keep the entire tree
# The idea is that when we do an inorder traversal on a valid BST, we should get the nodes in sorted order.
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        order = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            order.append(node.val)
            inorder(node.right)
            return

        inorder(root)

        for i in range(1, len(order)):
            if order[i] <= order[i - 1]:
                return False
        return True