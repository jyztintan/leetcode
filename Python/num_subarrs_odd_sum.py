class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        count, prefix_sum = 0, 0

        # Keep 2 parallel counts for 'odd' and 'even' parities
        odd = 0
        even = 1

        for num in arr:
            prefix_sum += num
            if prefix_sum % 2:
                count += even
                odd += 1
            else:
                count += odd
                even += 1

            count %= 10 ** 9 + 7

        return count
