# Solution 1: Using Greedy solution
class Solution:

    def jump(self, nums) -> bool:
        # The maximum index that can be reached with the current number of jumps
        limit = nums[0]

        # The furthest point that has been reached
        furthest = 0

        # Current number of jumps made
        jumps = 0

        # We can omit the last num as it is our target
        for i in range(len(nums) - 1):
            # We check the maximum index that can be reached
            # i + nums[i] represents the maximum index that can be reached if a jump is made from index i
            limit = max(limit, i + nums[i])

            # If the current index i is equals to the furthest point reached so far,
            # then we need another jump to get us further
            if i == furthest:
                jumps += 1
                furthest = limit

        return jumps

# Using Queue and BFS Traversal
# class Solution:
import queue

class Solution:

    def jump(self, nums) -> bool:
        if len(nums) == 1:
            return 0

        target = len(nums) - 1

        q = queue.Queue()
        visited = set()
        q.put((0, 0))
        while not q.empty():
            curr_pos, curr_jumps = q.get()
            for i in range(nums[curr_pos] + 1):
                if i + curr_pos == target:
                    return curr_jumps + 1
                if i + curr_pos not in visited:
                    q.put((i + curr_pos, curr_jumps + 1))
                    visited.add(i + curr_pos)

# nums = [2,3,1,1,4]
# nums = [2,3,0,1,4]
# nums = [10000, 10,10,10,10,13,14,134,3,232,34]
# print(Solution().jump(nums))