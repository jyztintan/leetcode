# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        q = collections.deque([(0,root)])
        ans = []
        while q:
            idx, ele = q.popleft()
            if len(ans) <= idx:
                ans.append([])
            ans[idx].append(ele.val)

            if ele.left:
                q.append((idx + 1, ele.left))
            if ele.right:
                q.append((idx + 1, ele.right))

        return ans
