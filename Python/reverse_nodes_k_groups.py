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

        # Found a full group of k nodes, so we need to reverse the group, then append the previous group's tail to this groups head
        if count == k:
            new_head = self.reverseList(head, k)
            head.next = self.reverseKGroup(pointer, k)
            return new_head

        return head

lst1 = ListNode(1, ListNode(4, ListNode(7, ListNode(9))))
lst2 = ListNode(2, ListNode(4, ListNode(5, ListNode(6))))
def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

printList(Solution().reverseKGroup(lst1, 2))
printList(Solution().reverseKGroup(lst2, 4))
