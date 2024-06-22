class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:

        # We keep 3 pointers for our algorithm: left, mid, right
        ans = num_odd = left = mid = 0

        # We increment the right pointer one index at a time
        for right in range(len(nums)):

            # If our right pointer has an odd value then we increment num_odd
            if nums[right] % 2:
                num_odd += 1

            # If num_odd exceeds k, then we need to increment the left pointer to remove the odd value from the left side
            # Note that num_odd can only exceed by at most 1
            # We short circuit left pointer to the most recent value of mid + 1 since mid will contain be the next odd value
            if num_odd > k:
                mid = left = mid + 1
                num_odd = k

            # If num_odd is equals k, we need to count the valid subarrays
            if num_odd == k:

                # Since the mid pointer is not odd, we continue to increment until it becomes an invalid subarray
                # This also guarantees us that the mid pointer will point to the next odd value
                while not nums[mid] % 2:
                    mid += 1

                # There are mid - left + 1 valid nice subarrays since there are no odd values within these range
                ans += mid - left + 1

        return ans

# nums = [1, 1, 2, 1, 1]
# print(Solution().numberOfSubarrays(nums, 3))


