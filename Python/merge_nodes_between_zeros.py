# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head):
        curr = head
        new_list = pointer = ListNode(0)
        accumulate = 0
        while curr:
            if curr.val == 0 and curr != head:
                pointer.next = ListNode(accumulate)
                pointer = pointer.next
                accumulate = 0

            accumulate += curr.val
            curr = curr.next

        return new_list.next

# lst1 = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(2, ListNode(4, ListNode(0)))))))
# lst2 = ListNode(2, ListNode(4, ListNode(5, ListNode(6))))
# def printList(node):
#     while node:
#         print(node.val, end=" -> ")
#         node = node.next
#     print("None")
#
# printList(Solution().mergeNodes(lst1))