class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        n, m = len(s), len(p)

        def match(s_ptr, p_ptr):
            # Target and string should finish at the same time
            if p_ptr == m:
                return s_ptr == n

            # No more characters to continue
            if s_ptr == n:
                # Check if its a '*' character then it can be 0 instances
                if p_ptr + 1 < m and p[p_ptr + 1] == '*':
                    return match(s_ptr, p_ptr + 2)
                return False

            # Calculated before
            if (s_ptr, p_ptr) in memo:
                return memo[(s_ptr, p_ptr)]

            first_match = p[p_ptr] == s[s_ptr] or p[p_ptr] == '.'

            # If the following character is a '*'
            if p_ptr + 1 < m and p[p_ptr + 1] == '*':
                # Don't use -> skip the character and '*'
                # Use '*' (if first character matches, move string pointer)
                memo[(s_ptr, p_ptr)] = (
                        match(s_ptr, p_ptr + 2) or
                        (first_match and match(s_ptr + 1, p_ptr))
                )
            else:
                # Simple case where characters must match or be '.'
                memo[(s_ptr, p_ptr)] = first_match and match(s_ptr + 1, p_ptr + 1)

            return memo[(s_ptr, p_ptr)]

        return match(0, 0)
