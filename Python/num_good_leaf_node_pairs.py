# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.leaves = {}
        self.height = {}
    def countPairs(self, root: TreeNode, distance: int) -> int:

        ans = [0]
        def count_leaves(root):
            if not root:
                return {}
            if not root.left and not root.right:
                return {1:1}
            left = count_leaves(root.left)
            right = count_leaves(root.right)
            d = {}
            for left_leaf in left:
                d[left_leaf + 1] = d.get(left_leaf + 1, 0) + left[left_leaf]
                for right_leaf in right:
                    if left_leaf + right_leaf <= distance:
                        ans[0] += left[left_leaf] * right[right_leaf]

            for right_leaf in right:
                d[right_leaf + 1] = d.get(right_leaf + 1, 0) + right[right_leaf]

            return d

        count_leaves(root)
        return ans[0]
