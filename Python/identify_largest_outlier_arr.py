class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        freq = Counter(nums)

        nums = set(nums)
        largest_outlier = - float('inf')

        for num in nums:
            # Check if it is possible for this num to be an outlier
            total_wo_outlier = total - num
            freq[num] -= 1
            # If the special numbers and its total exists, then the total_wo_outlier should be 2 x the total
            if total_wo_outlier % 2 == 0 and freq[total_wo_outlier // 2] > 0:
                largest_outlier = max(largest_outlier, num)
            freq[num] += 1

        return largest_outlier


