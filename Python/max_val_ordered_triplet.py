class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        highest_prev_num = -1
        highest_after_minus = -1
        ans = 0
        for num in nums:
            ans = max(ans, highest_after_minus * num)
            highest_after_minus = max(highest_after_minus, highest_prev_num - num)
            highest_prev_num = max(highest_prev_num, num)
        return ans
