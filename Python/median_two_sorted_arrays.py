class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:

        def find(k, nums1_start, nums1_end, nums2_start, nums2_end):

            if nums1_start > nums1_end:
                return nums2[k - nums1_start]
            if nums2_start > nums2_end:
                return nums1[k - nums2_start]

            nums1_idx, nums2_idx = (nums1_start + nums1_end) // 2, (nums2_start + nums2_end) // 2
            nums1_val, nums2_val = nums1[nums1_idx], nums2[nums2_idx]

            if nums1_idx + nums2_idx < k:
                # Remove the smaller, smaller left half
                if nums1_val > nums2_val:
                    return find(k, nums1_start, nums1_end, nums2_idx + 1, nums2_end)
                else:
                    return find(k, nums1_idx + 1, nums1_end, nums2_start, nums2_end)

            else:
                # Remove the larger, larger half
                if nums1_val > nums2_val:
                    return find(k, nums1_start, nums1_idx - 1, nums2_start, nums2_end)
                else:
                    return find(k, nums1_start, nums1_end, nums2_start, nums2_idx - 1)

        n = len(nums1) + len(nums2)

        if n % 2:
            return find(n // 2, 0, len(nums1) - 1, 0, len(nums2) - 1)
        return (find(n // 2 - 1, 0, len(nums1) - 1, 0, len(nums2) - 1)
                + find(n // 2, 0, len(nums1) - 1, 0, len(nums2) - 1)) / 2


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find(k, nums1_start, nums1_end, nums2_start, nums2_end):

            if nums1_start > nums1_end:
                return nums2[k - nums2_start]

            if nums2_start > nums2_end:
                return nums1[k - nums1_start]

            nums1_mid = (nums1_start + nums1_end) // 2
            nums2_mid = (nums2_start + nums2_end) // 2

            nums1_val, nums2_val = nums1[nums1_mid], nums2[nums2_mid]

            if k > nums1_mid + nums2_mid:
                # We remove the smaller of the smaller halves
                if nums1_val > nums2_val:
                    return find(k, nums1_start, nums1_end, nums2_mid + 1, nums2_end)
                else:
                    return find(k, nums1_mid + 1, nums1_end, nums2_start, nums2_end)

            else:
                # We remove the larger of the larger halves
                if nums1_val > nums2_val:
                    return find(k, nums1_start, nums1_mid - 1, nums2_start, nums2_end)
                else:
                    return find(k, nums1_start, nums1_end, nums2_start, nums2_mid - 1)

        n = len(nums1) + len(nums2)
        if n % 2:
            return find(n // 2, 0, len(nums1) - 1, 0, len(nums2) - 1)
        return (find(n // 2 - 1, 0, len(nums1) - 1, 0, len(nums2) - 1) + find(n // 2, 0, len(nums1) - 1, 0,
                                                                              len(nums2) - 1)) / 2

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:

        # Ensure nums1 is always the smaller array
        # If the initial nums1 is larger than nums2, we swap them
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        
        # This low-high range is the possible index such that it cleanly separates nums1 and nums2 into 2 subarrays,
        # with the left portion of both arrays forming the bottom half subarray
        low, high = 0, x
        while low <= high:
            
            # We try partitioning nums1 into half, then test if its a valid separation
            partition_x = (low + high) // 2

            # The remaining separation for nums2 must be half the number of total elements minus the partition in nums1
            partition_y = (x + y + 1) // 2 - partition_x

            # If partition_x is 0, there are no elements on the left side of nums1
            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]

            # If partition_x is length of nums1, there are no elements on the right side of nums1
            min_right_x = float('inf') if partition_x == x else nums1[partition_x]

            # If partition_y is 0, there are no elements on the left side of nums2
            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]

            # If partition_y is length of nums2, there are no elements on the right side of nums2
            min_right_y = float('inf') if partition_y == y else nums2[partition_y]

            # A correct partition is found when the max values in both left subarrays is lower than the min values of both right subarrays
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                break

            # If the maximum value in left subarray of nums1 is greater than right subarray of nums2, we need to decrease the partition index of nums1
            elif max_left_x > min_right_y:
                high = partition_x - 1

            # If the maximum value in left subarray of nums2 is greater than right subarray of nums1, we need to increase the partition index of nums1
            else:
                low = partition_x + 1

        # If total elements is odd, we need to take the average of the 2 middle elements
        if (x + y) % 2 == 0:
            return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2

        # Otherwise, we just return the maximum value in the left subarray
        return max(max_left_x, max_left_y)


# Test for same array
nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [1, 2, 3, 4, 5, 6]
assert Solution().findMedianSortedArrays(nums1, nums2) == 3.5

# Test for total length is odd
nums1 = [1, 3, 5, 7, 9]
nums2 = [2, 4, 6, 8]
assert Solution().findMedianSortedArrays(nums1, nums2) == 5

# Test for total length is even
nums1 = [1, 3, 5, 7, 9]
nums2 = [2, 4, 6, 8, 10]
assert Solution().findMedianSortedArrays(nums1, nums2) == 5.5

# Test for all elements are the same
nums1 = [1, 1, 1]
nums2 = [1]
assert Solution().findMedianSortedArrays(nums1, nums2) == 1

# Test for empty array
nums1 = [1, 2, 3, 4]
nums2 = []
assert Solution().findMedianSortedArrays(nums1, nums2) == 2.5