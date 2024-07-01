# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
        def removeNthFromEnd(self, head, n: int):
            count = 0
            pointer = head
            while pointer is not None:
                pointer = pointer.next
                count += 1
            idx = count - n
            if idx == 0:
                return head.next
            pointer = head
            for i in range(idx - 1):
                pointer = pointer.next
            pointer.next = pointer.next.next
            return head

# head = ListNode(1, ListNode(2))
# print(Solution().removeNthFromEnd(head, 1))