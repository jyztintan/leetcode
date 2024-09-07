# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k: int):
        if not head:
            return head
        curr = head
        count = 0

        while curr is not None:
            curr = curr.next
            count += 1

        start = head
        if (num := k % count) == 0:
            return start
        for i in range(count - num):
            start = start.next

        curr = start
        while curr.next != start:
            if curr.next is None:
                curr.next = head
            curr = curr.next
        curr.next = None
        return start


# list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# print(Solution().rotateRight(list, 2))
