# Using sets to avoid recomputation
class Solution:
    def canPartition(self, nums) -> bool:

        # If the total is not divisible by 2, then it obviously can't be partitioned
        total = sum(nums)
        if total % 2:
            return False

        # The target sum should be the total divided by 2
        target = total / 2

        # The idea is that we use sets so that we don't have to compute same values
        possible = set()
        possible.add(0)
        for num in nums:
            # If the negation of this number is inside, we can confidently say we found the partition
            if target - num in possible:
                return True
            # For each number, we can either choose to include or exclude in the component of the partition
            possible = possible.union([x + num for x in possible])
        return False
