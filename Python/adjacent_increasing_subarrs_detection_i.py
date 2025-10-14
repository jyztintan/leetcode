# O(N) Solution
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        is_increasing = [False] * n
        problems = deque()

        for i in range(n - 1):
            if nums[i] >= nums[i + 1]:
                problems.append(i)

        for right in range(k - 1, n):
            left = right - k + 1
            if problems and left > problems[0]:
                problems.popleft()
            if not problems or problems[0] > right - 1:
                is_increasing[right] = True

        for i in range(k - 1, n - k):
            if is_increasing[i] and is_increasing[i + k]:
                return True
        return False


# O(N * k) solution
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        for i in range(n - 2 * k + 1):
            increasing = True
            for j in range(k - 1):
                if nums[i + j] >= nums[i + j + 1]:
                    increasing = False
                    break
            for j in range(k, k + k - 1):
                if nums[i + j] >= nums[i + j + 1]:
                    increasing = False
                    break
            if increasing:
                return True
        return False