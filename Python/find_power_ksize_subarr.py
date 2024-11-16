class Solution:
    def resultsArray(self, nums, k: int):
        if k == 1:
            return nums
        n = len(nums)
        ans = []

        # Get initial window
        window_count = 1
        for i in range(1, k):
            if nums[i] == nums[i - 1] + 1:
                window_count += 1
        if window_count == k:
            ans.append(nums[i])
        else:
            ans.append(-1)

        # Slide the window and modify the count of consecutive numbers within the window by checking front and back
        for left in range(1, n - k + 1):
            right = left + k - 1
            if nums[left] == nums[left - 1] + 1:
                window_count -= 1
            if nums[right] == nums[right - 1] + 1:
                window_count += 1

            # If all consecutive, then add the right-most (highest) number, otherwise -1
            if window_count == k:
                ans.append(nums[right])
            else:
                ans.append(-1)

        return ans





nums = [1,2,3,4,3,2,5]
print(Solution().resultsArray(nums, 3))