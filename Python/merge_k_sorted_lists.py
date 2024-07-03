import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        heap = []
        for idx, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, idx, head))

        ans = current = ListNode(0)
        while heap:
            val, idx, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        return ans.next

lst1 = ListNode(1, ListNode(4, ListNode(7, ListNode(9))))
lst2 = ListNode(2, ListNode(4, ListNode(5, ListNode(6))))
def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")
printList(Solution().mergeKLists([lst1, lst2]))