class Solution(object):
    def minAreaRect(self, points):
        points_set = set(map(tuple, points))
        smallest = float('inf')

        # Iterate through every pair of points and see if their diagonals exist
        # If they do then we found a rectangle!
        for idx, (x1, y1) in enumerate(points):
            for x2, y2 in points[:idx]:
                if x1 != x2 and y1 != y2 and (x1, y2) in points_set and (x2, y1) in points_set:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    smallest = min(smallest, area)
        return smallest if smallest != float('inf') else 0
