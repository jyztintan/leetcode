# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        best = [0]

        def traverse(node):
            if not node:
                return 0, 0
            up, down = 1, 1
            if node.left:
                left_up, left_down = traverse(node.left)
                if node.left.val == node.val + 1:
                    up = max(up, left_up + 1)
                elif node.left.val == node.val - 1:
                    down = max(down, left_down + 1)

            if node.right:
                right_up, right_down = traverse(node.right)
                if node.right.val == node.val + 1:
                    up = max(up, right_up + 1)
                elif node.right.val == node.val - 1:
                    down = max(down, right_down + 1)
            best[0] = max(best[0], down + up - 1)
            return up, down

        traverse(root)
        return best[0]
