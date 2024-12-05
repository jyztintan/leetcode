# O(N) using queues and seems slightly more elegant
import queue


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_queue = queue.Queue()
        target_queue = queue.Queue()
        length = len(start)

        for ptr in range(length):
            start_char, target_char = start[ptr], target[ptr]
            if start_char != '_':
                start_queue.put((start_char, ptr))
            if target_char != '_':
                target_queue.put((target_char, ptr))

        if start_queue.qsize() != target_queue.qsize():
            return False

        while not start_queue.empty():
            char, idx = start_queue.get()
            target_char, target_idx = target_queue.get()
            if char != target_char:
                return False
            if char == 'L':
                if idx < target_idx:
                    return False
            elif char == 'R':
                if idx > target_idx:
                    return False
        return True


# O(N) but seems a bit clunky
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        length = len(start)
        start = list(start)

        stack = []
        # Check for rights
        for ptr in range(length):
            if start[ptr] == 'R':
                stack.append(ptr)
            elif start[ptr] == 'L':
                if stack:
                    return False

            if target[ptr] == 'R':
                # There exist an R in target that is to the left of a matching R in start string
                if not stack:
                    return False
                swap = stack.pop()
                start[ptr], start[swap] = start[swap], start[ptr]

        if stack:
            return False

        # Check for left
        for ptr in range(length - 1, -1, -1):
            if start[ptr] == 'L':
                stack.append(ptr)
            elif start[ptr] == 'R':
                if stack:
                    return False

            if target[ptr] == 'L':
                # There exist an L in target that is to the left of a matching R in start string
                if not stack:
                    return False
                swap = stack.pop()
                start[ptr], start[swap] = start[swap], start[ptr]

        if stack:
            return False

        return True


# start = "_L__R__R_"
# target = "L______RR"
# print(Solution().canChange(start, target))
# assert Solution().canChange("R", "_") == False
