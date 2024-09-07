from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def dfs(node, curr):
            if not node:
                return False
            if node.val != curr.val:
                return False

            curr = curr.next
            if curr is None:
                return True
            return dfs(node.left, curr) or dfs(node.right, curr)

        if dfs(root, head):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

# Creating leaf nodes
leaf1 = TreeNode(1)
leaf6 = TreeNode(6)
leaf3 = TreeNode(3)

# Creating other nodes based on the structure
node8 = TreeNode(8, leaf1, leaf3)
node2_right = TreeNode(2, leaf6, node8)
node2_left = TreeNode(2, TreeNode(1), None)

node4_right = TreeNode(4, node2_right, None)
node4_left = TreeNode(4, None, node2_left)

root = TreeNode(1, node4_left, node4_right)

# Create Linked List
head = ListNode(4, ListNode(2, ListNode(8)))

print(Solution().isSubPath(head, root))

