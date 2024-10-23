import heapq
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root, k: int) -> int:

        # Perform BFS on the nodes
        level_sums = []
        q = Queue()
        q.put(root)

        while not q.empty():
            curr_level_sum = 0
            for i in range(q.qsize()):
                node = q.get()
                curr_level_sum += node.val
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)

            heapq.heappush(level_sums, -curr_level_sum)

        if len(level_sums) < k:
            return -1

        for i in range(k - 1):
            heapq.heappop(level_sums)
        return -heapq.heappop(level_sums)


