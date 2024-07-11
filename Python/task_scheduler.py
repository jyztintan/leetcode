import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks, n: int) -> int:

        # Get frequency of each task
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        # Push frequency of each task into a max heap, we dont care about the task name
        heap = []
        heapq.heapify(heap)
        for task, num in freq.items():
            heapq.heappush(heap, -num)

        # Keeps track of time period passed
        count = 0

        # Keeps track of tasks that are on "time out" -> cannot be done as not long enough interval has passed
        prev_tasks = deque()

        # While there are still tasks to be done, either available now or on "time out"
        while heap or prev_tasks:
            count += 1

            # Schedule to complete the next available task
            if heap:
                num = heapq.heappop(heap) + 1
                # If this task needs to be done again, we take note of the interval
                if num != 0:
                    prev_tasks.append((num, count + n))

            # Schedule back the repeated task
            if prev_tasks and prev_tasks[0][1] == count:
                heapq.heappush(heap, prev_tasks.popleft()[0])

        return count

# tasks = ["A","A","A","B","B","B"]
# print(Solution().leastInterval(tasks, 2))
