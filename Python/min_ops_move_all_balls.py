class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n

        left_balls = 0
        move_right = 0

        right_balls = 0
        move_left = 0

        for idx in range(n):
            ans[idx] += move_right
            if boxes[idx] == '1':
                left_balls += 1
            move_right += left_balls

            idx = n - 1 - idx
            ans[idx] += move_left
            if boxes[idx] == '1':
                right_balls += 1
            move_left += right_balls

        return ans
