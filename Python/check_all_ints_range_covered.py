class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums = [0] * 52
        for start, end in ranges:
            nums[start] += 1
            nums[end + 1] -= 1

        run_sum = 0
        for i in range(left):
            run_sum += nums[i]

        for i in range(left, right + 1):
            run_sum += nums[i]
            if not run_sum:
                return False
        return True
