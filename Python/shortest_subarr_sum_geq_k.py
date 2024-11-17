from collections import deque


class Solution:
    def shortestSubarray(self, nums, k: int) -> int:
        if len(nums) == 1:
            return 1 if nums[0] >= k else -1

        best = float('inf')
        n = len(nums)

        prefix_sums = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

        possible = deque()
        for right in range(n + 1):
            # Remove the left-most num and see if the subarr is still >= k
            while possible and prefix_sums[right] - prefix_sums[possible[0]] >= k:
                best = min(best, right - possible.popleft())
                if best == 1:
                    return 1

            # Any subarray formed using the prev index that satisfies >= k can also be formed using right as the limit
            while possible and prefix_sums[right] <= prefix_sums[possible[-1]]:
                possible.pop()

            possible.append(right)

        if best == float('inf'):
            return -1
        return best


nums = [1, 2, 1, 8, 7, 11]
print(Solution().shortestSubarray(nums, 16))


