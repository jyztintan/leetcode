# The rationale used here is that the number of deletions is the number of b's to the left
# plus the number of a's to the right.
class Solution:
    def minimumDeletions(self, s: str) -> int:
        # We count the number of b's to the left and a's to the right
        left_b, right_a = 0, s.count('a')
        best = float('inf')
        for c in s:
            # If the current char is a, then we subtract one a from the right
            if c == 'a':
                right_a -= 1
                best = min(best, right_a + left_b)
            else:
                # If the current char is b, then we add 1 to the count of b's for subsequent iterations
                best = min(best, right_a + left_b)
                left_b += 1
        return best
