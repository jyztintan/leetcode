# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return []

        curr_level = [root]
        while curr_level:
            next_level = []

            highest = - float('inf')
            for node in curr_level:
                highest = max(highest, node.val)

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            curr_level = next_level
            ans.append(highest)
        return ans
