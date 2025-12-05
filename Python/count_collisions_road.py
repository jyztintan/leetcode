# Big brain solution is that all "outer" cars will escape
# All other "inner" cars must then collide minimum/maximum once
class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        left, right = 0, n - 1
        while left < n and directions[left] == "L":
            left += 1
        while right >= 0 and directions[right] == "R":
            right -= 1
        count = 0
        for i in range(left, right + 1):
            if directions[i] != 'S':
                count += 1
        return count

class Solution:
    def countCollisions(self, directions: str) -> int:
        right, left = 0, 0
        stop = 0
        bang = 0
        for c in directions:
            if c == "L":
                if right:
                    bang += right + 1
                    right = 0
                    stop = 1
                elif stop:
                    bang += 1
            elif c == "R":
                right += 1
                stop = 0
            else:
                stop = 1
                if right:
                    bang += right
                    right = 0
        return bang

