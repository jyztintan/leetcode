class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):

        copy = {None:None}

        curr = head
        while curr:
            curr_copy = Node(curr.val)
            copy[curr] = curr_copy
            curr = curr.next

        curr = head
        while curr:
            copy[curr].next = copy[curr.next]
            copy[curr].random = copy[curr.random]
            curr = curr.next

        return copy[head]
