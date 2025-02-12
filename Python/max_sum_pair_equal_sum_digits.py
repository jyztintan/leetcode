class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sums = {}
        best = -1
        for num in nums:
            digit_sum = 0
            for digit in str(num):
                digit_sum += int(digit)
            if digit_sum in digit_sums:
                best = max(best, num + digit_sums[digit_sum])
                digit_sums[digit_sum] = max(digit_sums[digit_sum], num)
            else:
                digit_sums[digit_sum] = num
        return best
