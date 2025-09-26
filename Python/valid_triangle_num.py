# Total time complexity : O(N**2)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        # Fix the third length # O(N)
        for third in range(n - 1, 1, -1):
            first = 0
            second = third - 1
            # See how many pairs we can pick within this bounds (O(N) loop)
            while first < second:
                if nums[first] + nums[second] > nums[third]:
                    count += second - first
                    second -= 1
                else:
                    first += 1
        return count
