# O(N) Algorithm
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        s = s + s
        return goal in s

# O(N^2) Algorithm :(
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n, m = len(s), len(goal)
        if n != m:
            return False
        for goal_ptr in range(m):
            check_ptr = 0
            while s[check_ptr] == goal[goal_ptr]:
                check_ptr += 1
                if check_ptr == n:
                    return True
                goal_ptr += 1
                if goal_ptr == m:
                    goal_ptr = 0
        return False


