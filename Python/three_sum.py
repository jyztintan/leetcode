class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # First sort the nums array to make life easier :)
        nums.sort()

        # Create answer list
        ans = []
        end = len(nums) - 1

        # loop through each element in the sorted nums array
        for i, num in enumerate(nums):

            # Check that it is not 0 to prevent index error (via short-circuiting)
            # If the new num is a duplicate of the previous, skip it. We don't want duplicate 3 sums.
            if i != 0 and num == nums[i-1]:
                continue

            # The left pointer starts from the element following 'num'
            # The right pointer starts from the end of the nums array
            left = i + 1
            right = end

            # When the 2 pointers overlap, we can stop the process
            while left < right:
                total = nums[left] + nums[right] + num

                # If total = 0, we found a successful 3sum array!
                if total == 0:
                    ans.append([num, nums[left], nums[right]])

                    # We don't want the same elements so make sure to move the pointers
                    # We also don't want duplicate values so keep doing it until we get a new value
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                # If total is less than 0, then we need higher values so move left pointer up.
                elif total < 0:
                    left += 1

                # If total is more than 0, then we need lower values so move right pointer down.
                else:
                    right -= 1

        return ans

# sol = Solution()
# nums = [1, -1, -1, 0]
# print(sol.threeSum(nums))