# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions):
        nodes = {}
        descendants = set()
        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            descendants.add(child)
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        for key in nodes:
            if key not in descendants:
                return nodes[key]

descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
print(Solution().createBinaryTree(descriptions))