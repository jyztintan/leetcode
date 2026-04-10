class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        num_idx = defaultdict(list)
        for idx, num in enumerate(nums):
            num_idx[num].append(idx)

        best = inf
        for num in num_idx:
            n = len(num_idx[num])
            lst = num_idx[num]
            if n < 3:
                continue
            for i in range(2, n):
                dist = (lst[i] - lst[i - 2]) * 2
                best = min(best, dist)
        if best == inf:
            return -1
        return best
