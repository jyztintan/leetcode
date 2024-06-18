"""
This solution sorts jobs by their difficulty level and then sorts each work by its ability.
Then, we can iterate through the worker array and find the maximum profit easily as we can assume that
each subsequent workers has access to all previous works as well since the difficulty and ability levels
are non-decreasing.

Time Complexity - O(nlogn + nlogn + n) = O(nlogn)
1. Sorting the jobs by their difficulty
2. Sorting work by their ability
3. Iterating through the sorted worker array and incrementing max_profit at that point in time

Space Complexity - O(n)
Jobs array has size of n and worker array is sorted in place.
"""

class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker) -> int:

        # Group jobs together by their respective difficulty and profit
        # Then, sort these jobs by their difficulty level
        jobs = sorted(zip(difficulty, profit))

        # This keeps track of the max_profit each work has access to at any point in time
        max_profit = 0

        # This is the pointer for our jobs array
        j = 0

        # This is the max total accumulated profit to be output
        ans = 0

        # Sort workers so that each subsequent worker has at least the same ability as the previous worker
        worker.sort()

        for work in worker:

            # j < len(jobs) to ensure we do not go out of range
            # We increment the pointer for all jobs that have difficulty <= to this work's ability
            while j < len(jobs) and work >= jobs[j][0]:

                # Note that a job with a higher difficulty does not mean higher profit.
                # Hence, we still always keep the highest profit as we want to maximise it, irrelevant to difficulty.
                max_profit = max(max_profit, jobs[j][1])
                j += 1

            # Increment the max_profit that this worker can do
            ans += max_profit

        return ans

# sol = Solution()
# difficulty = [2,4,6,8,10]
# profit = [10,20,30,40,50]
# worker = [4,5,6,7]
# print(sol.maxProfitAssignment(difficulty, profit, worker))
# difficulty = [85,47,57]
# profit = [24,66,99]
# worker = [40,25,25]
# print(sol.maxProfitAssignment(difficulty, profit, worker))
