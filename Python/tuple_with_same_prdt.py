class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = defaultdict(int)
        n = len(nums)

        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                if products[product]:
                    count += 8 * products[product]
                products[product] += 1
        return count
