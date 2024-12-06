# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        # Dummy head
        head = curr = ListNode(-1000)
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return head.next

# Basic Test Case
list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))
merged = Solution().mergeTwoLists(list1, list2)
assert merged.val == 1
assert merged.next.val == 2
assert merged.next.next.val == 3
assert merged.next.next.next.val == 4
assert merged.next.next.next.next.val == 5
assert merged.next.next.next.next.next.val == 6
