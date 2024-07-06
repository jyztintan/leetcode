# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""
        q = collections.deque([root])
        ans = []
        while q:
            ele = q.popleft()
            if not ele:
                ans.append("null")
                continue

            ans.append(str(ele.val))
            q.append(ele.left)
            q.append(ele.right)

        return ','.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        root = TreeNode(int(data[0]))
        queue = collections.deque([root])
        pointer = 1

        while queue:
            node = queue.popleft()

            if pointer < len(data) and data[pointer] != 'null':
                node.left = TreeNode(int(data[pointer]))
                queue.append(node.left)
            pointer += 1
            if pointer < len(data) and data[pointer] != 'null':
                node.right = TreeNode(int(data[pointer]))
                queue.append(node.right)
            pointer += 1

        return root

