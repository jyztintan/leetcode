# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def addTwoNumbers(self, l1, l2):

        # Keep track of the first node
        first = child = ListNode()

        # Keep track of current carry
        carry = 0

        # While there are subsequent numbers or there is a carry
        while l1 or l2 or carry:

            # We create a new node for the new digit
            to_add = carry

            # If l1 is not None, then we add its value to the new digit
            if l1:
                to_add += l1.val
                l1 = l1.next

            # If l2 is not None, then we add its value to the new digit
            if l2:
                to_add += l2.val
                l2 = l2.next

            # This new digit will be the child of the previous list node
            child.next = ListNode(to_add % 10)
            child = child.next

            # Take note of the carry over digit
            carry = to_add // 10
        return first.next

# l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = ListNode(5, ListNode(6, ListNode(4)))
# print(Solution().addTwoNumbers(l1, l2))