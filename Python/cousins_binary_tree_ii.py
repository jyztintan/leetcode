# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def replaceValueInTree(self, root):
        curr = [(root, root)]

        while curr:
            level = {}
            next_level = []

            # Initial BFS sweep, get total value in a level
            for par, child in curr:
                level[par] = level.get(par, 0) + child.val

            # All SIBLINGS should have the same values
            total = sum(level.values())
            updated = {par: total - val for par, val in level.items()}

            # Second BFS sweep to modify values based on parents
            for i in range(len(curr)):
                par, child = curr.pop()
                child.val = updated[par]

                if child.left:
                    next_level.append((child, child.left))

                if child.right:
                    next_level.append((child, child.right))

            curr = next_level

        return root




