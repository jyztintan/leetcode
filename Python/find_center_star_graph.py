class Solution:
    # The rationale behind this solution is that in a star graph, there are exactly n - 1 edges,
    # with every edge containing the center point, either as the 1st or 2nd point
    # Hence, we can just check for the overlapping point in any 2 given edges
    def findCenter(self, edges) -> int:
        u1, v1 = edges[0]
        u2, v2 = edges[1]
        if u1 == v2 or u1 == u2:
            return u1
        return v1