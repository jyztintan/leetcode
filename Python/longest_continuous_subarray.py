from collections import deque
class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        left = ans = 0

        # non-decreasing sort of elements in current subarray
        min_deque = deque()

        # non-increasing sort of elements in current subarray
        max_deque = deque()

        for right in range(len(nums)):

            # If this new element is less than the previous element(s) in the min_deque, those previous element(s) will never be the minimum element
            # Hence we can pop these elements
            while min_deque and nums[right] < min_deque[-1]:
                min_deque.pop()

            # If this new element is more than the previous element(s) in the max_deque, those previous element(s) will never be the maximum element
            # Hence we can pop these elements
            while max_deque and  nums[right] > max_deque[-1]:
                max_deque.pop()

            min_deque.append(nums[right])
            max_deque.append(nums[right])

            # Check if the maximum and minimum elment within the subarray exceeds the limit
            while max_deque[0] - min_deque[0] > limit:

                # Since it exceeds the limit, we get rid of the left-most element

                # Ensure that if the min is the left-most element, we pop it out since we no longer include it in our subarray
                if nums[left] == min_deque[0]:
                    min_deque.popleft()

                # Ensure that if the max is the left-most element, we pop it out since we no longer include it in our subarray
                if nums[left] == max_deque[0]:
                    max_deque.popleft()

                # Move the left-pointer up
                left += 1

            # Get the size of the new valid subarray and check if it is the largest
            ans = max(ans, right - left + 1)

        return ans

# nums = [10,1,2,4,7,2]
# print(Solution().longestSubarray(nums, 6))
# nums = [4,2,2,2,4,4,2,2]
# print(Solution().longestSubarray(nums, 2))
# nums = [1,5,6,7,8,10,6,5,6]
# print(Solution().longestSubarray(nums, 4))
