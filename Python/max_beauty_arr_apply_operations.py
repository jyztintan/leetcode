from typing import List

# Sliding Window
# Time: O(NlogN) Space: O(n)
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        max_beauty = 0

        for right in range(len(nums)):
            while nums[left] + k < nums[right] - k:
                left += 1
            max_beauty = max(max_beauty, right - left + 1)
        return max_beauty


# Overlapping intervals
# Time: O(N) Space: O(max(nums)))
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1

        highest = max(nums)
        freq = [0] * (highest + 1)

        for num in nums:
            freq[max(0, num - k)] += 1
            if num + k + 1 <= highest:
                freq[num + k + 1] -= 1


        curr_streak = 0
        max_streak = 0

        for count in freq:
            curr_streak += count
            max_streak = max(max_streak, curr_streak)
        return max_streak

# Time: O(NlogN) Space: O(N)
# Overlapping intervals
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        events = []
        for num in nums:
            events.append((num - k, 1))
            events.append((num + k, -1))

        events.sort()
        curr_streak = 0
        max_streak = 0

        for num, event in events:
            curr_streak += event
            max_streak = max(max_streak, curr_streak)
        return max_streak
