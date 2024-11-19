class Solution:
    def maximumSubarraySum(self, nums, k: int) -> int:

        curr = 0
        seen = {}
        duplicates = set()
        # Initialise the window
        for i in range(k):
            num = nums[i]
            curr += num
            seen[num] = seen.get(num, 0) + 1
            if seen[num] > 1:
                duplicates.add(num)

        best = 0
        if not duplicates:
            best = curr

        # Slide the window right
        for left in range(len(nums) - k):
            # Remove left-most
            left_most = nums[left]
            curr -= left_most
            seen[left_most] -= 1
            if seen[left_most] == 1:
                duplicates.remove(left_most)

            right_most = nums[left + k]
            curr += right_most
            seen[right_most] = seen.get(right_most, 0) + 1
            if seen[right_most] > 1:
                duplicates.add(right_most)

            if not duplicates:
                best = max(best, curr)

        return best


# nums = [1,1,1,7,8,9]
# print(Solution().maximumSubarraySum(nums, 3))
