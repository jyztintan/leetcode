class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        largest_subarr = None
        curr_neg_subarr = None
        curr_pos_subarr = None

        for num in nums:
            if curr_pos_subarr is None:
                curr_pos_subarr = curr_neg_subarr = largest_subarr = num
                continue
            if num < 0:
                curr_neg_subarr, curr_pos_subarr = curr_pos_subarr, curr_neg_subarr

            curr_pos_subarr = max(curr_pos_subarr * num, num)
            curr_neg_subarr = min(curr_neg_subarr * num, num)
            largest_subarr = max(largest_subarr, curr_pos_subarr)

        return largest_subarr
