# Big brain O(N) solution which basically stores the sums we have previously computed
# Kind of like the same logic as 2-sum
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # The empty subarray has sum 0 and occurs once
        prefix_sum_count = {0: 1}

        curr = 0
        count = 0
        for num in nums:
            curr += num
            count += prefix_sum_count.get(curr - k, 0)
            prefix_sum_count[curr] = prefix_sum_count.get(curr, 0) + 1
        return count


# O(N^2) Solution: TLE
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = [0]
        n = len(nums)

        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)

        count = 0
        for idx in range(n + 1):
            for end in range(idx + 1, n + 1):
                if prefix_sums[end] - prefix_sums[idx] == k:
                    count += 1
        return count
