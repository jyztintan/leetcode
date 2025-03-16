class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        curr = 0
        # Set up first window
        for ptr in range(ones):
            curr += data[ptr]

        best = ones - curr
        for left in range(len(data) - ones):
            curr -= data[left]
            curr += data[left + ones]
            best = min(best, ones - curr)
        return best
