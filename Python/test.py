from typing import Optional
from collections import deque


class JobQueue:
    def __init__(self):
        self.first_half = deque()
        self.second_half = deque()

    def __repr__(self):
        return str(self.queue)

    def push(self, priority: str, job_name: str) -> None:
        """
            If priority "high" push to the front of the queue,
            If priority "low" push to the back of the queue,
            If priority "medium" push to the middle of the queue;
                Cases:
                    - Even number existing in the queue:
                        push in the exact middle,
                        i.e. ['j1','j2'] push 'j3' -> ['j1','j3','j2']
                    - Odd number existing in the queue
                        push in the 'Right' spot in the middle
                        i.e. ['j1','j2', 'j3'] push 'j4' -> ['j1','j2', 'j4', 'j3']
            If priority not "low", "medium" or "high" raise exception.
        """
        if priority == 'high':
            self.first_half.appendleft(job_name)  # O(1)
        elif priority == 'low':
            self.second_half.append(job_name)  # O(1)
        else:
            self.second_half.appendleft(job_name)  # O(1)
            # n = len(self.queue)
            # mid = n//2
            # if n % 2:
            #     mid += 1
            # self.queue.insert(mid, job_name) # O(n)

        # Check that the deques are balanced and even them out if necessary
        # Invariant: The length of the first deque can only be 1 greater than the length of the second deque
        # Invariant: The length of the first deque should never be less than the second deque
        if len(self.first_half) < len(self.second_half):
            transfer = self.second_half.popleft()
            self.first_half.append(transfer)
        elif len(self.first_half) > len(self.second_half) + 1:
            transfer = self.first_half.pop()
            self.second_half.appendleft(transfer)



    def pop(self) -> Optional[str]:
        """Return the job at the front of the queue. If queue empty return None"""
        if not self.queue:
            return None
        return self.queue.popleft  # O(1)

    def combine(self):
        lst = []
        lst.extend(self.first_half.copy())
        lst.extend(self.second_half.copy())
        return lst


# Test for push 'high' priority
jq = JobQueue()
jq.push("high", "job1")
jq.push("high", "job2")
assert jq.combine() == ['job2', 'job1']

# Test for push 'low' priority
jq1 = JobQueue()
jq1.push("low", "job1")
jq1.push("low", "job2")
assert jq1.combine() == ['job1', 'job2']

# Test for inserting middle for odd length queue
jq2 = JobQueue()
jq2.push("low", "job1")
jq2.push("low", "job2")
jq2.push("high", "job3")
jq2.push("medium", "job4")
assert jq2.combine() == ['job3', 'job1', 'job4', 'job2']

# Test for inserting middle for even length queue
jq2 = JobQueue()
jq2.push("low", "job1")
jq2.push("low", "job2")
jq2.push("medium", "job3")
assert jq2.combine() == ['job1', 'job3', 'job2']

# def average(lst):
#     if not lst:
#         raise Exception("List length is 0. Cannot compute average")
#     total = sum(lst)
#     return total/len(lst)

# lst = [9.4, 1000, 35, 493, 5]
# lst = list(range(1,4))

# print(average(lst))

# try:
#     print(average([]))
# except Exception as e:
#     print(e)