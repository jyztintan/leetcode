# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head, k):
        prev = None
        curr = head
        while k > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            k -= 1
        return prev

    def reverseKGroup(self, head, k: int):
        pointer = head
        count = 0
        while pointer and count < k:
            pointer = pointer.next
            count += 1

        if count == k:
            new_head = self.reverseList(head, k)

            # original head is now the tail
            head.next = self.reverseKGroup(pointer, k)
            return new_head
        return head


# Iterative:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next

        def reverse(start, end):
            prev = None
            curr = start
            while curr != end:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        new = prev = ListNode(0)
        prev.next = head
        for _ in range(count // k):
            group_start = group_end = prev.next
            for i in range(k - 1):
                group_end = group_end.next

            next_group_start = group_end.next
            new_start = reverse(group_start, next_group_start)
            prev.next = new_start
            new_end = group_start
            new_end.next = next_group_start
            prev = new_end

        return new.next

# lst1 = ListNode(1, ListNode(4, ListNode(7, ListNode(9))))
# lst2 = ListNode(2, ListNode(4, ListNode(5, ListNode(6))))
# def printList(node):
#     while node:
#         print(node.val, end=" -> ")
#         node = node.next
#     print("None")
#
# printList(Solution().reverseKGroup(lst1, 2))
# printList(Solution().reverseKGroup(lst2, 4))
