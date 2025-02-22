# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        depth = 0
        val_str = ""
        nodes_depth = []

        # Create and process nodes in order
        for c in traversal:
            # End of number
            if c == "-" and val_str:
                val = int(val_str)
                node = TreeNode(val)
                nodes_depth.append((node, depth))
                depth = 1
                val_str = ""
            # Start of number
            elif c != "-":
                val_str += c
                continue
            else:
                depth += 1

        # Process last node
        val = int(val_str)
        node = TreeNode(val)
        nodes_depth.append((node, depth))

        st = [nodes_depth[0]]
        for node, depth in nodes_depth[1:]:
            while st and st[-1][1] > depth:
                st.pop()

            if depth == st[-1][1]:
                sibling, _ = st.pop()
                parent, _ = st.pop()
                parent.left = sibling
                parent.right = node
            elif depth > st[-1][1]:
                parent, _ = st[-1]
                if parent.left:
                    parent.right = node
                else:
                    parent.left = node
            st.append((node, depth))

        return nodes_depth[0][0]
