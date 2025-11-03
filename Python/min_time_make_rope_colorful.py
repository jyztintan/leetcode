class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ptr = 0
        n = len(colors)
        remove = 0

        while ptr < n:
            curr = colors[ptr]
            total = neededTime[ptr]
            best = neededTime[ptr]
            while ptr < n - 1 and colors[ptr + 1] == curr:
                ptr += 1
                total += neededTime[ptr]
                best = max(best, neededTime[ptr])
            remove += total - best
            ptr += 1
        return remove
