from collections import defaultdict
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Step 1: We first get the mapping of each number to its respective frequency
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        # Step 2: We then get the mapping of frequency to number(s) instead
        increasing = defaultdict(list)
        for key, val in d.items():
            increasing[val].append(key)

        # Step 3: We iterate through the frequencies to get our answer
        ans = []
        # We want the frequencies in increasing order
        for freq in sorted(increasing.keys()):
            # We want the numbers of same frequencies to be in decreasing order
            for num in sorted(increasing[freq], reverse=True):
                ans.extend([num] * freq)
        return ans

# nums = [1,1,2,2,2,3]
# print(Solution().frequencySort(nums))