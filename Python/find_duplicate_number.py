class Solution:

    # Solution requires a constant space solution without modifying input array
    def findDuplicate(self, nums) -> int:

        # Since values in nums array are guaranteed to be [1, n] and there are n + 1 numbers
        # We can treat these values as pointers to help us find the cycle
        # We use Floyd's Tortoise-Hare Cycle-Finding Algorithm to help us find the duplicate in O(1) space
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        new_slow = 0
        while slow != new_slow:
            slow = nums[slow]
            new_slow = nums[new_slow]
        return slow