class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad
        n = len(nums)
        nums = [1] + nums + [1]
        memo = {}

        def pop(left, right):
            if left > right:
                return 0
            if (left, right) in memo:
                return memo[(left, right)]

            best = 0
            # Try popping each balloon
            for idx in range(left, right + 1):
                # Coins earned = left boundary * right boundary * balloon
                coins = nums[left - 1] * nums[idx] * nums[right + 1]

                # Plus the coins gained from the subarrays formed
                coins += pop(left, idx - 1)
                coins += pop(idx + 1, right)

                best = max(best, coins)

            memo[(left, right)] = best
            return best

        return pop(1, n)
