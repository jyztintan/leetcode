class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = -float('inf')
        used = set()

        for num in nums:
            # We try to greedily use the next smallest valid number
            new_num = min(num + k, max(prev + 1, num - k))
            if new_num not in used:
                used.add(new_num)
            prev = new_num
        return len(used)
