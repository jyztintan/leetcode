class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node'):
        ans = []

        def dfs(node):
            if not node:
                return
            if node.children:
                for child in node.children:
                    dfs(child)
            ans.append(node.val)

        dfs(root)
        return ans
