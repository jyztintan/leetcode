class Solution:
    def maxWidthRamp(self, nums) -> int:
        mono_st = []
        for i, num in enumerate(nums):
            if not mono_st or mono_st[-1][0] > num:
                mono_st.append((num, i))

        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            while mono_st and mono_st[-1][0] <= nums[i]:
                ans = max(ans, i - mono_st[-1][1])
                mono_st.pop()
        return ans


nums = [9,8,1,0,1,9,4,0,4,1]
print(Solution().maxWidthRamp(nums))



