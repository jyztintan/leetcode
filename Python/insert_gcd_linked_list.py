# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head):
        if not head:
            return head

        # Euclid's Algorithm :)))))))))))))
        def find_gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        curr = head
        while nxt:= curr.next:
            gcd = find_gcd(curr.val, nxt.val)
            curr.next = ListNode(gcd, nxt)
            curr = nxt
        return head


