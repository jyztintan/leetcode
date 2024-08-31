class Solution:
    def maxCoins(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]

        nums = [1] + nums + [1]
        memoized = {}

        def pop(left, right):
            if left > right:
                return 0
            if (left, right) in memoized:
                return memoized[(left, right)]
            # Try "leaving out" each balloon
            best = 0
            for i in range(left, right + 1):
                # Number of coins will be the boundaries * the balloon we left out
                coins = nums[left - 1] * nums[i] * nums[right + 1]
                # Including the max coins we get from the subarrays formed
                coins += pop(left, i - 1)
                coins += pop(i + 1, right)
                best = max(best, coins)
            memoized[(left, right)] = best
            return best

        return pop(1, n)

nums = [3,1,5,8]
print(Solution().maxCoins(nums))

