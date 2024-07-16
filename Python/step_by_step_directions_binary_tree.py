# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root, startValue: int, destValue: int) -> str:

        start_dir = []
        dest_dir = []
        def dfs(node, target, directions, res):
            if not node:
                return False

            if node.val == target:
                res.append("".join(directions))
                return True

            # Search in the left subtree
            directions.append("L")
            if dfs(node.left, target, directions, res):
                return True
            directions.pop()

            # Search in the right subtree
            directions.append("R")
            if dfs(node.right, target, directions, res):
                return True
            directions.pop()

            return False

        dfs(root, startValue, [], start_dir)
        dfs(root, destValue, [], dest_dir)

        start_dir = start_dir[0]
        dest_dir = dest_dir[0]

        ptr = 0
        while ptr < len(start_dir) and ptr < len(dest_dir) and start_dir[ptr] == dest_dir[ptr]:
            ptr += 1

        ans = "U" * (len(start_dir) - ptr) + dest_dir[ptr:]
        return ans



node3 = TreeNode(3)
node6 = TreeNode(6)
node4 = TreeNode(4)
node1 = TreeNode(1, left=node3)
node2 = TreeNode(2, left=node6, right=node4)
root = TreeNode(5, left=node1, right=node2)

# Create solution instance
solution = Solution()
startValue = 3
destValue = 6
# Execute the test
print(solution.getDirections(root, startValue, destValue))
