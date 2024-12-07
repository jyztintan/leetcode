# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        levelorder = ""
        q = [root]
        while q:
            new_q = []
            for node in q:
                if not node:
                    levelorder += 'None,'
                    continue
                levelorder += str(node.val) + ','
                new_q.append(node.left)
                new_q.append(node.right)
            q = new_q
        return levelorder

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = queue.Queue()
        q.put(root)
        i = 1
        while not q.empty() and i < len(nodes):
            node = q.get()
            if nodes[i] != 'None':
                left = TreeNode(int(nodes[i]))
                node.left = left
                q.put(left)
            i += 1
            if nodes[i] != 'None':
                right = TreeNode(int(nodes[i]))
                node.right = right
                q.put(right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))