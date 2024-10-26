import heapq
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)
class Solution:
    def treeQueries(self, root, queries):
        max_path = {}
        heights = defaultdict(list)
        location = {}

        # DFS
        def dfs(node, height):
            location[node] = height
            if node.left and node.right:
                dfs(node.left, height + 1)
                dfs(node.right, height + 1)
                max_path[node] = max(max_path[node.left], max_path[node.right]) + 1
            elif node.left:
                dfs(node.left, height + 1)
                max_path[node] = max_path[node.left] + 1
            elif node.right:
                dfs(node.right, height + 1)
                max_path[node] = max_path[node.right] + 1
            else:
                max_path[node] = 0

        dfs(root, 0)

        ans = {}

        def query(node, height, max_val):
            if not node:
                return
            ans[node.val] = max_val

            if node.left:
                query(node.right, height + 1, max(max_val, height + 1 + max_path[node.left]))
            else:
                query(node.right, height + 1, max(max_val, height))

            if node.right:
                query(node.left, height + 1, max(max_val, height + 1 + max_path[node.right]))
            else:
                query(node.left, height + 1, max(max_val, height))

        query(root, 0, 0)
        return [ans[q] for q in queries]
