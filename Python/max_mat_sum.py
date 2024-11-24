class Solution:
    def maxMatrixSum(self, matrix) -> int:
        ans = 0
        lowest = float('inf')
        count_negs = 0

        # Iterate through matrix
        for row in matrix:
            for ele in row:
                # Count number of initial negatives
                if ele < 0:
                    count_negs += 1
                # Get the lowest absolute value
                lowest = min(lowest, abs(ele))
                ans += abs(ele)

        # If there are an odd number of negative numbers initially, then we should keep the lowest one negative
        # If there an even number of negative numbers, there will be a way we can flip all to become all positive
        if count_negs % 2:
            ans -= lowest * 2
        return ans


