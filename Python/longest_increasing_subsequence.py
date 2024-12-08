# O(NlogN) as we employ binary search to find the best subsequence
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest_sub = []
        for num in nums:
            idx = bisect_left(longest_sub, num)

            # The current number is > all numbers in the curr subsequence
            if idx == len(longest_sub):
                longest_sub.append(num)
            else:
                longest_sub[idx] = num

        return len(longest_sub)



# O(N^2) time complexity, where iterate through all the elements to the left, for every element
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # Initially, the longest subsequence is just the number itself
        best = [1] * n
        for right in range(n):
            for left in range(right):
                # Add the number to the existing subsequence
                if nums[right] > nums[left]:
                    best[right] = max(best[right], best[left] + 1)
        return max(best)
