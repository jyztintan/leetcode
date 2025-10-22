from collections import defaultdict
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        max_num = max(nums) + k
        window = [0] * (max_num + 2)

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
            window[max(0, num - k)] += 1
            window[num + k + 1] -= 1

        curr = 0
        best = -1
        for num, delta in enumerate(window):
            curr += delta
            within_k = max(0, curr - freq[num])
            best = max(best, min(within_k, numOperations) + freq[num])
        return best
