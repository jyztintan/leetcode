# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rightSideView(self, root):

        res = []
        def check_by_height(root, height):
            if not root:
                return
            if len(res) == height:
                res.append(root.val)
            check_by_height(root.right, height + 1)
            check_by_height(root.left, height + 1)
            return

        check_by_height(root, 0)
        return res

