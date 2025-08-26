class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        best = [0, 0]
        for length, width in dimensions:
            diagonal = math.sqrt(length * length + width * width)
            if diagonal > best[0]:
                best = [diagonal, length * width]
            elif diagonal == best[0]:
                best[1] = max(best[1], length * width)
        return best[1]
