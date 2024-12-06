from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # We maintain 2 invariants
        # 1) The deque is always strictly decreasing
        # 2) The left-most element in the deque will always contain the max element of the window
        dq = deque()

        largests = []
        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        largests.append(nums[dq[0]])

        for i in range(k, len(nums)):
            # If the max element is no longer in the window - maintain invariant #2
            if dq and dq[0] == i - k:
                dq.popleft()
            # Pop all elements that are now 'useless' - maintain invariant #1
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            dq.append(i)
            largests.append(nums[dq[0]])
        return largests


# Simple test case
assert Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]

# Negative numbers
assert Solution().maxSlidingWindow([-1,-3,-1,-3,-5,-3,-6,-7], 3) == [-1, -1, -1, -3, -3, -3]

# Strictly increasing
assert Solution().maxSlidingWindow([1,2,3,4,5,6,7], 4) == [4,5,6,7]

# Strictly decreasing
assert Solution().maxSlidingWindow([7, 6, 5, 4, 3, 2, 1], 3) == [7, 6, 5, 4, 3]

# Same number
assert Solution().maxSlidingWindow([7,7,7,7,7], 2) == [7,7,7,7]

# k == 1
assert Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 1) == [1,3,-1,-3,5,3,6,7]

# k == n
assert Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 8) == [7]
