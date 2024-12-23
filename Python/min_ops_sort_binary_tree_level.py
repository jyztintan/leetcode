# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        curr_level = [root]
        total_swaps = 0
        while curr_level:
            next_level = []
            next_level_vals = []

            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                    next_level_vals.append(node.left.val)
                if node.right:
                    next_level.append(node.right)
                    next_level_vals.append(node.right.val)
            total_swaps += self.min_swaps(next_level_vals)

            curr_level = next_level
        return total_swaps

    def min_swaps(self, nums: List[int]) -> int:
        curr_pos = {val: idx for idx, val in enumerate(nums)}
        target = sorted(nums)

        swaps = 0
        for idx, num in enumerate(target):
            if num == nums[idx]:
                continue

            swaps += 1

            wrong_num = nums[idx]
            wrong_pos = curr_pos[num]
            curr_pos[wrong_num] = wrong_pos
            nums[wrong_pos] = wrong_num

        return swaps
