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

# nums1 = list(range(6, 9))
# nums2 = list(range(1, 5))
# print(Solution().findMedianSortedArrays(nums1, nums2))
