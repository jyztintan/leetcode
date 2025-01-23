class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        prefix_sum = 0

        for i in range(n):
            prefix_sum += nums[i]
            answer = max(answer, ceil(prefix_sum / (i + 1)))

        return answer
