import collections

class Solution:
    def maxSlidingWindow(self, nums, k: int):

        left = 0
        res = []
        deque = collections.deque()

        for right in range(len(nums)):

            # If our new number is greater than values from the deque, we remove those values because they will no longer be relevant
            while deque and nums[deque[-1]] < nums[right]:
                deque.pop()
            deque.append(right)

            # If our left pointer has exceeded the leftmost index value of the deque, then we should remove it
            if left > deque[0]:
                deque.popleft()

            # We only want to start after processing the first window
            if (right + 1) >= k:
                # The left most value in the deque is guaranteed to have the greatest value, so we just append it
                res.append(nums[deque[0]])
                left += 1

        return res

# nums = [1,3,-1,-3,5,3,6,7]
# print(Solution().maxSlidingWindow(nums, 3))
