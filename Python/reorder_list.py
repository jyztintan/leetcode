# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        tail = None
        while head:
            next = head.next
            head.next = tail
            tail = head
            head = next
        return tail
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Find the middle of the linked list using a slow and fast pointer
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        second_half = self.reverseList(slow.next)
        # Split the list into two halves
        slow.next = None

        # Merge the two halves
        first_half = head
        while second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half, second_half = temp1, temp2

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
Solution().reorderList(head)