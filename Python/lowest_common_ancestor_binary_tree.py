# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(curr, node, path):
            if not curr:
                return False
            if curr == node:
                return path
            if ans := dfs(curr.left, node, path + [curr.left]):
                return ans
            return dfs(curr.right, node, path + [curr.right])

        path_p = dfs(root, p, [root])
        path_q = dfs(root, q, [root])

        n = len(path_p)
        m = len(path_q)

        ptr = 1
        while True:
            if ptr >= n or ptr >= m or path_p[ptr] != path_q[ptr]:
                return path_p[ptr - 1]
            ptr += 1

# root = TreeNode(3)
# p = root.left = TreeNode(5)
# root.right = TreeNode(1)
#
# root.left.left = TreeNode(6)
# root.left.right = TreeNode(2)
#
# root.right.left = TreeNode(0)
# root.right.right = TreeNode(8)
#
# root.left.right.left = TreeNode(7)
# q = root.left.right.right = TreeNode(4)
# print(Solution().lowestCommonAncestor(root, p, q))
