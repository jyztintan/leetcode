import queue


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node'):
        if not root:
            return []

        q = queue.Queue()
        q.put((root))
        ans = []

        while not q.empty():
            level = []
            for _ in range(q.qsize()):
                node = q.get()
                level.append(node.val)
                if node.children:
                    for child in node.children:
                        q.put(child)
            ans.append(level)
        return ans


node5 = Node(5)
node6 = Node(6)
node3 = Node(3, [node5, node6])
node4 = Node(4)
node2 = Node(2)
node1 = Node(1, [node2, node3, node4])
print(Solution().levelOrder(node1))
