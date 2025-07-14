# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = head.val
        head = head.next
        while head:
            num <<= 1
            num += head.val
            head = head.next
        return num
