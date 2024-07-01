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

# lst = ListNode(1, ListNode(2, ListNode(3)))
# print(Solution().reverseList(lst))