class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        ptr = 0
        for idx, num in enumerate(nums):
            if num not in seen:
                nums[ptr] = nums[idx]
                ptr += 1
                seen.add(num)
        for _ in range(ptr, len(nums)):
            nums.pop()
        return len(seen)
