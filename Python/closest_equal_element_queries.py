class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        num_idx = defaultdict(list)

        for idx, num in enumerate(nums):
            num_idx[num].append(idx)

        n = len(nums)
        resp = []
        for q in queries:
            target = nums[q]
            matches = num_idx[target]
            if len(matches) == 1:
                resp.append(-1)
                continue
            pos = bisect.bisect_left(matches, q)
            prev_idx = matches[pos - 1]
            next_idx = matches[(pos + 1) % len(matches)]

            d1 = abs(q - prev_idx)
            d2 = abs(next_idx - q)

            resp.append(min(d1, n - d1, d2, n - d2))

        return resp

