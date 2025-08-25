# Sliding Window, O(N) time, O(1) space
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        buffer = 0
        best = 0
        left = 0

        for right, num in enumerate(nums):
            if num == 0:
                buffer += 1

            while buffer > 1:
                if nums[left] == 0:
                    buffer -= 1
                left += 1

            best = max(best, right - left)
        return best

# Partitioning: O(N) time, O(N) space
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums.append(0)
        partition = []
        curr = 0
        for num in nums:
            if num:
                curr += 1
            else:
                partition.append(curr)
                curr = 0

        if len(partition) == 0:
            return 0
        elif len(partition) == 1:
            return partition[0] - 1

        best = 0
        for idx in range(len(partition) - 1):
            best = max(best, partition[idx] + partition[idx + 1])
        return best
