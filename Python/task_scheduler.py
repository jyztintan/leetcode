import heapq
from collections import deque, defaultdict


class Solution:
    def leastInterval(self, tasks, n: int) -> int:

        # Get frequency of each task
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1

        # Push frequency of each task into a max heap, we dont care about the task name
        sorted_freq = [-count for count in freq.values()]
        heapify(sorted_freq)

        time = 0
        timeout = deque()

        # While there are still tasks to be done, either available now or on "time out"
        while sorted_freq or timeout:

            # Schedule back the repeated task
            if timeout and timeout[0][0] == time:
                _, task_freq = timeout.popleft()
                heappush(sorted_freq, task_freq)
            time += 1

            if sorted_freq:
                count = heappop(sorted_freq)
                # If this task needs to be done again, we take note of the interval
                if count + 1 < 0:
                    timeout.append((time + n, count + 1))
        return time
