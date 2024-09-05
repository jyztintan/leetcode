# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive DFS
class Solution:
    def findTarget(self, root, k: int) -> bool:
        complement = set()
        def dfs(node):
            if not node:
                return False
            if node.val in complement:
                return True

            complement.add(k - node.val)
            if dfs(node.left):
                return True
            if dfs(node.right):
                return True
            return False

        return dfs(root)

# Iterative DFS
class Solution:
    def findTarget(self, root, k: int) -> bool:
        st = [root]
        complement = set()
        while st:
            curr = st.pop()
            if curr.val in complement:
                return True
            complement.add(k - curr.val)
            if curr.left:
                st.append(curr.left)
            if curr.right:
                st.append(curr.right)
        return False

