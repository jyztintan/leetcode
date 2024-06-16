class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        # This represents the next test case that we are unsure if our nums array can sum to
        test = 1

        # This is the pointer in our sorted nums array
        index = 0

        # This variable keeps track of the number of times we need to "add" a value in our nums array
        ans = 0

        # Ensure all test cases from [1,n] are accounted for
        while test <= n:

            # If our pointer is out of range then the only way we can solve this test case is to add the value itself
            # If our current pointer in the nums array has value that exceeds the test case, we have no choice but to also add the value itself
            # In both scenarios mentioned above, adding that test case itself will increase our possible reachable values by that test case value
            # Hence, our range expands from [1, 2 * test - 1] and the next test case we would need to test for is 2 * test
            if index >= len(nums) or nums[index] > test:
                ans += 1
                test += test

            # If our current test case is <= nums' pointer value, then we can also expand our reachable values by this pointer's value
            # We then increment the pointer
            else:
                test += nums[index]
                index += 1
        return ans


# sol = Solution()
# nums = [1, 5, 10]
# print(sol.minPatches(nums, 20))
# nums = [1,2,31,33]
# print(sol.minPatches(nums, 2147483647))