class Solution:
    def canSortArray(self, nums) -> bool:

        # Keep track of previous and current contiguous subarray with the same number of set bits
        prev = [float('inf'), 0]
        curr = [float('inf'), 0]
        curr_bits = bin(nums[0]).count('1')

        for num in nums:
            count = bin(num).count('1')
            # Still in same segment, just modify curr as appropriate
            if curr_bits == count:
                curr[0] = min(curr[0], num)
                curr[1] = max(curr[1], num)
            # New segment to create
            else:
                # Check that the current segment is "valid",
                # lowest element in the curr segment should be < highest ele in prev segment
                if curr[0] < prev[1]:
                    return False

                # This curr segment becomes the prev segment
                prev = curr

                # Create new segment
                curr_bits = count
                curr = [num, num]

        # Final check that the last segment is valid
        if curr[0] < prev[1]:
            return False
        return True

# print(Solution().canSortArray([75,34,30]))