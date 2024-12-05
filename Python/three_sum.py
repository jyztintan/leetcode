class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = set()
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                continue
            seen.add(num)
            target = - num
            complements = set()
            for possible in nums[i + 1:]:
                if possible in complements:
                    ans.add(tuple(sorted([num, target - possible, possible])))
                complements.add(target - possible)
        return list(ans)


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # First sort the nums array to make life easier :)
        nums.sort()
        ans = []
        end = len(nums) - 1

        for i, num in enumerate(nums):

            # If the new num is a duplicate of the previous, skip it. We don't want duplicate 3 sums.
            if i != 0 and num == nums[i-1]:
                continue

            left = i + 1
            right = end

            while left < right:
                total = nums[left] + nums[right] + num

                if total == 0:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # We also don't want duplicate values so keep doing it until we get a new value
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return ans

# sol = Solution()
# nums = [1, -1, -1, 0]
# print(sol.threeSum(nums))
