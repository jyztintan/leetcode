class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        lat, lon = 0, 0
        best = 0
        for i, c in enumerate(s):
            if c == 'N':
                lat += 1
            elif c == 'S':
                lat -= 1
            elif c == 'E':
                lon += 1
            else:
                lon -= 1
            best = max(best, min(abs(lat) + abs(lon) + k * 2, i + 1))
        return best
