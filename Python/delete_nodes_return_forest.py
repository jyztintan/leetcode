class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root, to_delete):

        to_delete = set(to_delete)
        forest = []

        def dfs(node):
            if not node:
                return None

            # Perform any deletion within the deeper subtrees first
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in to_delete:
                if node.left:
                    # It is now its own subtree
                    forest.append(node.left)
                if node.right:
                    # It is now its own subtree
                    forest.append(node.right)
                return None

            return node


        modified_root = dfs(root)
        # Check if the root should be deleted, otherwise it is also a valid tree that should be added to the forest
        if modified_root:
            forest.append(modified_root)
        return forest