from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        remove = set(nums)
        dummy = dummy_head = ListNode()
        curr = head
        while curr != None:
            if curr.val not in remove:
                dummy.next = curr
                dummy = curr
            curr = curr.next
            dummy.next = None

        return dummy_head.next

nums = [9,2]
head = ListNode(2, ListNode(4, ListNode(5)))
print(Solution().modifiedList(nums, head))
