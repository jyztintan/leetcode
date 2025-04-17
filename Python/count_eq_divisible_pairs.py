class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        freq = defaultdict(set)
        count = 0
        for idx, num in enumerate(nums):
            for prev in freq[num]:
                if (idx * prev) % k == 0:
                    count += 1
            freq[num].add(idx)
        return count
