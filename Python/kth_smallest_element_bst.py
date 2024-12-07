# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]

        def inorder(node):
            if not node:
                return

            if (ans := inorder(node.left)) is not None:
                return ans
            count[0] += 1
            if count[0] == k:
                return node.val
            if (ans := inorder(node.right)) is not None:
                return ans

        return inorder(root)
