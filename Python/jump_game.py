# Solution 1: Using Greedy solution
# Moving goal backwards
class Solution:

    def canJump(self, nums) -> bool:
        target = len(nums) - 1

        for i in range(target, -1, -1):
            # We can guarantee that the target can be reached if we reach this index.
            # Hence, we can set this index as the new target
            if nums[i] + i >= target:
                target = i
        # Since we have iteratively modified the goal, if it reaches 0, it means that we are guaranteed
        # to be able to reach the actual end goal
        return target == 0

# Moving forward
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        ptr = 0
        furthest = nums[0]
        while ptr < n - 1 and ptr <= furthest:
            furthest = max(furthest, ptr + nums[ptr])
            ptr += 1
        return furthest >= n - 1

# Using Stack and DFS Traversal
# class Solution:
#
#     def canJump(self, nums) -> bool:
#         target = len(nums) - 1
#
#         st = []
#         visited = set()
#         st.append(0)
#         while st:
#             curr = st.pop()
#             for i in range(nums[curr] + 1):
#                 if i + curr == target:
#                     return True
#                 if i + curr not in visited:
#                     st.append(i + curr)
#                     visited.add(i + curr)
#         return False

# nums = [3,2,1,0,4]
# print(Solution().canJump(nums))