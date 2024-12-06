# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

class Solution:
    def reverseList(self, head):
        tail = None
        while head:
            next = head.next
            head.next = tail
            tail = head
            head = next
        return tail

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        order = []
        curr = head
        while curr:
            order.append(curr)
            curr = curr.next
        for i in range(1, len(order)):
            node = order[-i]
            node.next = order[-i-1]
        head.next = None
        return order[-1]

lst = ListNode(1, ListNode(2, ListNode(3)))
print(Solution().reverseList(lst))