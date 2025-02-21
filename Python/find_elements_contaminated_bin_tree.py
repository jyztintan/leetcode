# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.elements = set()
        root.val = 0
        st = [root]

        while st:
            node = st.pop()
            self.elements.add(node.val)
            if node.left:
                st.append(node.left)
                node.left.val = node.val * 2 + 1

            if node.right:
                st.append(node.right)
                node.right.val = node.val * 2 + 2

    def find(self, target: int) -> bool:
        return target in self.elements

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
