class Solution:
    def maxDistance(self, position, m: int) -> int:

        position.sort()

        # This method helps us to count the number of balls that can be placed, given a minimum force
        # It assumes that force <= max(position) - min(position) and that force > 0
        def get_min_force(force):
            count = 1
            dist = position[0]
            for pos in position:
                if pos >= dist + force:
                    dist = pos
                    count += 1
            return count

        # The minimum force must be 1 since balls cannot be in the same position
        low = 1

        # The maximum min force between balls would when m = 2 and the balls are placed in the first and last bins
        high = max(position) - min(position)
        best = -1

        while low <= high:
            mid = (low + high) // 2
            num_balls = get_min_force(mid)

            # If the number of balls we can put is less than m, then we need to decrease the force
            if num_balls < m:
                high = mid - 1

            # If the number of balls we can put is greater than or equals to m, we can try to increase the force
            if num_balls >= m:
                best = mid
                low = mid + 1

        return best

position = [1,2,3,4,5,6,7,8,9,10]
print(Solution().maxDistance(position, 4))
position = [5,4,3,2,1,1000000000]
print(Solution().maxDistance(position, 2))
