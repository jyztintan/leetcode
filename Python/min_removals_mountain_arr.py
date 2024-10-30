class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # Guess that each index is the peak
        longest_increasing = [0] * n
        longest_decreasing = [0] * n

        for i in range(n):
            peak = nums[i]
            best = 1
            for j in range(i):
                if peak > nums[j]:
                    best = max(best, longest_increasing[j] + 1)
            longest_increasing[i] = best

        for i in range(n - 1, -1, -1):
            peak = nums[i]
            best = 1
            for j in range(n - 1, i, -1):
                if peak > nums[j]:
                    best = max(best, longest_decreasing[j] + 1)
            longest_decreasing[i] = best

        best = 0
        for i in range(n):
            if longest_increasing[i] > 1 and longest_decreasing[i] > 1:
                best = max(best, longest_increasing[i] + longest_decreasing[i] - 1)

        return n - best


nums = [100,92,89,77,74,66,64,66,64]
print(Solution().minimumMountainRemovals(nums))