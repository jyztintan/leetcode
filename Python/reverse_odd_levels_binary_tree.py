# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
        curr_level = [root]

        while True:
            next_level = []
            vals = []

            # Get order of nodes
            for node in curr_level:
                # Check if there exists a lower level
                if node.left is None:
                    break
                next_level.append(node.left)
                vals.append(node.left.val)
                next_level.append(node.right)
                vals.append(node.right.val)

            if not vals:
                break

            level += 1
            ptr = -1
            if level % 2:
                for node in curr_level:
                    node.left.val = vals[ptr]
                    ptr -= 1
                    node.right.val = vals[ptr]
                    ptr -= 1

            curr_level = next_level

        return root
