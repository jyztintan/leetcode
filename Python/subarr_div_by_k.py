class Solution(object):
    def subarraysDivByK(self, nums, k):
        seen = {}
        cumulative = 0
        total = 0
        for num in nums:
            cumulative = (cumulative + num) % k
            seen[cumulative] = seen.get(cumulative, 1 if cumulative == 0 else 0)
            total += seen[cumulative]
            seen[cumulative] += 1
        return total


# Testing
# sol = Solution()
# nums = [4,5,0,-2,-3,1]
# print(sol.subarraysDivByK(nums, 5))
