# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return False

        subtrees = []

        def get_root_val(node):
            if not node:
                return 0
            total = node.val
            total += get_root_val(node.left)
            total += get_root_val(node.right)
            subtrees.append(total)
            return total

        total_sum = get_root_val(root)
        if total_sum == 0:
            return len(set(subtrees)) == 1 or subtrees.count(0) == 2
        return total_sum / 2 in subtrees
