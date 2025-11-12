class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones:
            return n - ones

        subarr = float('inf')
        for i in range(n):
            div = nums[i]
            for j in range(i + 1, n):
                div = gcd(div, nums[j])
                if div == 1:
                    subarr = min(subarr, j - i)

        if subarr == float('inf'):
            return -1
        return subarr + n - 1
