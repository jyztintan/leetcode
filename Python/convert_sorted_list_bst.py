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
    def sortedListToBST(self, head):
        def get_middle(lst):
            if not lst:
                return
            mid = slow = fast = lst
            while fast and fast.next:
                mid = slow
                slow = slow.next
                fast = fast.next.next
            return mid

        def build_tree(node):
            if not node:
                return
            predec_mid = get_middle(node)
            if not predec_mid.next:
                return TreeNode(predec_mid.val)
            mid = predec_mid.next
            predec_mid.next = None
            # Recurse with shortened link list
            left_sub = build_tree(node)

            suc_mid = mid.next
            right_sub = build_tree(suc_mid)

            tree = TreeNode(mid.val, left_sub, right_sub)
            return tree
        return build_tree(head)

