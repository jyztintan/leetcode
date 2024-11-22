class Solution:
    def maxEqualRowsAfterFlips(self, matrix) -> int:
        count = {}
        for row in matrix:
            rep = "".join(map(lambda x:"1" if x == row[0] else "0", row))
            count[rep] = count.get(rep, 0) + 1

        return max(count.values())
