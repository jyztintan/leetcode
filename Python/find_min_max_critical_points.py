# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head):

        pointer = 0
        minimum = float('inf')
        maximum = -float('inf')
        prev = head
        curr = head.next
        first_cp, last_cp = 0, 0
        isFirst = True

        # While the curr node is not the last node
        while curr.next:

            # Check if current node is a critical node
            if (prev.val > curr.val and curr.next.val > curr.val) or (prev.val < curr.val and curr.next.val < curr.val):
                if isFirst:
                    first_cp = pointer
                    isFirst = False
                else:
                    minimum = min(minimum, pointer - last_cp)
                last_cp = pointer
            # Update new values
            prev = curr
            curr = curr.next
            pointer += 1

        if minimum == float('inf'):
            return [-1, -1]
        return [minimum, last_cp - first_cp]

lst = ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))
print(Solution().nodesBetweenCriticalPoints(lst))