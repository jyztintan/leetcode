from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        curr = head
        while curr is not None:
            n += 1
            curr = curr.next

        size = n // k
        additional = n % k

        ans = []
        curr = head
        while curr is not None:
            ans.append(curr)
            skip = size - 1
            if additional:
                skip += 1
                additional -= 1
            for i in range(skip):
                curr = curr.next

            temp = curr.next
            curr.next = None
            curr = temp

        if k > n:
            for i in range(k - n):
                ans.append(None)

        return ans

list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(Solution().splitListToParts(list, 5))
