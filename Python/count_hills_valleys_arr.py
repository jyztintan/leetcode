class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        dedup = []
        for i, num in enumerate(nums):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            dedup.append(num)

        count = 0
        for i in range(1, len(dedup) - 1):
            if dedup[i - 1] < dedup[i] > dedup[i + 1]:
                count += 1
            elif dedup[i - 1] > dedup[i] < dedup[i + 1]:
                count += 1
        return count
