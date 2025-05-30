# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        new = head
        while new:
            for _ in range(m - 1):
                if new.next:
                    new = new.next
            temp = new
            for _ in range(n):
                if new.next:
                    new = new.next
            temp.next = new.next
            new = new.next
        return head
